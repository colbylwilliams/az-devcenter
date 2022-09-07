# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=logging-fstring-interpolation

from azure.cli.core.util import is_guid
from knack.log import get_logger
from knack.prompting import prompt_y_n
from knack.util import CLIError

from ._client_factory import (devcenter_client_factory,
                              devcenter_dataplane_client_factory,
                              get_graph_client)

logger = get_logger(__name__)

DEVBOX_USER_ROLE_ID = '45d50f46-0b78-4001-a660-4198cbe8cd05'
PROJECT_ADMIN_ROLE_ID = '331c37c6-af14-46d9-b9f4-e1909e1b95a0'


# def dc_test(cmd, user='me'):
#     pass


def dc_upgrade(cmd, version=None, prerelease=False):
    from azure.cli.core.extension.operations import update_extension

    from ._utils import get_github_release

    release = get_github_release(version=version, prerelease=prerelease)

    index = next((a for a in release['assets']
                  if 'index.json' in a['browser_download_url']), None)

    index_url = index['browser_download_url'] if index else None

    if not index_url:
        raise CLIError(
            f"Could not find index.json asset on release {release['tag_name']}. "
            'Specify a specific prerelease version with --version '
            'or use latest prerelease with --pre')

    update_extension(cmd, extension_name='dc', index_url=index_url)

# ----------------
# dc box
# ----------------


def _get_boxes(cmd, client, dev_center, project_names=None, pool_names=None, user_ids=None):  # pylint: disable=unused-argument
    # if user_ids and 'me' in user_ids:
    #     from azure.cli.core._profile import Profile
    #     user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()
    #     user_ids.remove('me')
    #     user_ids.append(user_id)

    # get all projects in the devcenter
    logger.info(f'Getting projects in DevCenter: {dev_center} ...')
    projects = client.project.list_by_dev_center()
    projects = list(projects)

    # make sure we got a list of projects
    if not projects or len(projects) == 0:
        logger.warning(f'No projects found in devcenter: {dev_center}. Make sure you have at least Reader role on '
                       'the projects.')
        return []

    # filter projects by name (if specified)
    if project_names:
        projects = [p for p in projects if p.name in project_names]
        # ensure we have at least one project
        if len(projects) == 0:
            logger.error(f'No projects found in devcenter {dev_center} matching names: {project_names}. '
                         'Make sure you typed the names correctly and have at least Reader role on the projects.')
            return []
        # ensure we found all the projects we were looking for
        for name in project_names:
            if name not in [p.name for p in projects]:
                logger.error(f'No projects found in devcenter {dev_center} matching name: {name}. '
                             'Make sure you typed the name correctly and have at least Reader role on the project.')
                return []

    logger.info(f' found {len(projects)} {"project" if len(projects) == 1 else "projects"}: '
                f'{[n.name for n in projects]}')

    # would be ideal to create an odata query based in the projects/pools/users
    # but it doesn't look like the --filter argment is respected by the dataplane
    # get all dev-boxes in the devcenter
    all_boxes = client.dev_box.list()
    all_boxes = list(all_boxes)

    if not all_boxes or len(all_boxes) == 0:
        logger.warning(f'No boxes found in devcenter: {dev_center}. Make sure you have the DevCenter Project Admin '
                       'role on the projects.')
        return []

    return_boxes = []

    for project in projects:
        logger.info('')
        logger.info(f'Getting boxes in {project.name} ...')

        # filter boxes for the project
        project_boxes = [b for b in all_boxes if b.project_name == project.name]

        if not project_boxes or len(project_boxes) == 0:
            logger.warning(f'No boxes found in project: {project.name}. If this is incorrect, make sure you have the '
                           'DevCenter Project Admin role on the project.')
            continue

        # filter boxes by users (if specified)
        if user_ids:
            project_boxes = [b for b in project_boxes if b.user in user_ids]
            if len(project_boxes) == 0:
                logger.info(f' no boxes found matching users: {user_ids}')
                continue

        # filter boxes by pools (if specified)
        if pool_names:
            project_boxes = [b for b in project_boxes if b.pool_name in pool_names]
            if len(project_boxes) == 0:
                logger.info(f' no boxes found matching pools: {pool_names}')
                continue

        corect_grammer = " matching specified pools/users" if user_ids or pool_names else ""
        logger.info(f' found {len(project_boxes)} {"box" if len(project_boxes) == 1 else "boxes"}{corect_grammer}: '
                    f'{[b.name for b in project_boxes]}')

        if len(project_boxes) > 0:
            return_boxes.extend(project_boxes)

    return return_boxes


def _start_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    client = devcenter_dataplane_client_factory(cmd.cli_ctx, dev_center)
    boxes = _get_boxes(cmd, client, dev_center, project_names, pool_names, user_ids)

    not_deallocated = [b for b in boxes if b.power_state.lower() != 'deallocated']
    if not_deallocated and len(not_deallocated) > 0:
        corect_grammer = "box because it isn't" if len(not_deallocated) == 1 else "boxes because they aren't"
        logger.info(f' skipping {len(not_deallocated)} {corect_grammer} deallocated: '
                    f'{[b.name for b in not_deallocated]}')

    # filter out boxes that are not deallocated
    boxes = [b for b in boxes if b.power_state.lower() == 'deallocated']

    # if we still have boxes to start, start them
    if len(boxes) > 0:

        if not yes and not prompt_y_n(f'\nAre you sure you want to start {len(boxes)} boxes?', default='n'):
            return None

        logger.info(f' starting {len(boxes)} {"box" if len(boxes) == 1 else "boxes"}')

        for box in boxes:
            logger.info(f' starting {box.name}...')
            client.dev_box.begin_start(box.project_name, box.name, user_id=box.user)

    return _get_boxes(cmd, client, dev_center, project_names, pool_names, user_ids)


def _stop_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    client = devcenter_dataplane_client_factory(cmd.cli_ctx, dev_center)
    boxes = _get_boxes(cmd, client, dev_center, project_names, pool_names, user_ids)

    not_running = [b for b in boxes if b.power_state.lower() != 'running']
    if not_running and len(not_running) > 0:
        corect_grammer = "box because it isn't" if len(not_running) == 1 else "boxes because they aren't"
        logger.info(f' skipping {len(not_running)} {corect_grammer} running: {[b.name for b in not_running]}')

    # filter out boxes that are not running
    boxes = [b for b in boxes if b.power_state.lower() == 'running']

    # if we still have boxes to stop, stop them
    if len(boxes) > 0:

        if not yes and not prompt_y_n(f'\nAre you sure you want to stop {len(boxes)} boxes?', default='n'):
            return None

        logger.info(f' stopping {len(boxes)} {"box" if len(boxes) == 1 else "boxes"}')

        for box in boxes:
            logger.info(f' stopping {box.name}...')
            client.dev_box.begin_stop(box.project_name, box.name, user_id=box.user)

    return _get_boxes(cmd, client, dev_center, project_names, pool_names, user_ids)


def list_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None):
    client = devcenter_dataplane_client_factory(cmd.cli_ctx, dev_center)
    return _get_boxes(cmd, client, dev_center, project_names, pool_names, user_ids)


def start_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    return _start_boxes(cmd, dev_center, project_names, pool_names, user_ids, yes)


def stop_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    return _stop_boxes(cmd, dev_center, project_names, pool_names, user_ids, yes)


def list_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None):
    client = devcenter_dataplane_client_factory(cmd.cli_ctx, dev_center)
    return _get_boxes(cmd, client, dev_center, [project_name], pool_names, user_ids)


def start_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None, yes=False):
    return _start_boxes(cmd, dev_center, [project_name], pool_names, user_ids, yes)


def stop_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None, yes=False):
    return _stop_boxes(cmd, dev_center, [project_name], pool_names, user_ids, yes)


# ----------------
# dc project user
# ----------------

def _check_user_licenses(cmd, user):
    if user == 'me':
        from azure.cli.core._profile import Profile
        user = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()

    from azure.cli.command_modules.role.custom import _resolve_object_id

    try:
        user_id = _resolve_object_id(cmd.cli_ctx, user, fallback_to_object_id=True)

        client = get_graph_client(cmd.cli_ctx)
        result = client._send('GET', f'/users/{user_id}/licenseDetails')  # pylint: disable=protected-access

        licenses = [l for l in result if 'skuPartNumber' in l and l['skuPartNumber'] in ['SPE_E3', 'SPE_E5']]

        if len(licenses) > 0:
            logger.info(f'{user} has valid licenses: {[l["skuPartNumber"] for l in licenses]}')
            return (True, f'{user} has valid licenses: {[l["skuPartNumber"] for l in licenses]}')

        logger.info(f'{user} does not have a valid license')
        return (False, f'{user} does not have a valid license')

    except Exception as ex:  # pylint: disable=broad-except
        logger.debug(ex)
        return (False, f'{ex}')


def _add_project_role(role, cmd, resource_group_name, project_name, user_id='me'):
    from azure.cli.command_modules.role.custom import create_role_assignment
    client = devcenter_client_factory(cmd.cli_ctx)
    project = client.projects.get(resource_group_name, project_name)

    if user_id.lower() == 'me':
        from azure.cli.core._profile import Profile
        user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()
        return create_role_assignment(cmd, role=role, assignee=user_id, scope=project.id)

    if is_guid(user_id):
        return create_role_assignment(cmd, role=role, assignee_object_id=user_id,
                                      assignee_principal_type='User', scope=project.id)

    return create_role_assignment(cmd, role=role, assignee=user_id, scope=project.id)


def _remove_project_role(role, cmd, resource_group_name, project_name, user_id='me'):
    from azure.cli.command_modules.role.custom import delete_role_assignments
    client = devcenter_client_factory(cmd.cli_ctx)
    project = client.projects.get(resource_group_name, project_name)

    if user_id.lower() == 'me':
        from azure.cli.core._profile import Profile
        user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()

    return delete_role_assignments(cmd, role=role, assignee=user_id, scope=project.id)


# ----------------
# dc project user
# ----------------

def add_project_user(cmd, resource_group_name, project_name, user_id='me', skip_license_check=False):
    if not skip_license_check:
        check = _check_user_licenses(cmd, user_id)
        if not check[0]:
            raise CLIError(check[1])

    return _add_project_role(DEVBOX_USER_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def remove_project_user(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(DEVBOX_USER_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def dc_user_check(cmd, user='me'):
    check = _check_user_licenses(cmd, user)
    return check[1]

# ----------------
# dc project admin
# ----------------


def add_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _add_project_role(PROJECT_ADMIN_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def remove_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(PROJECT_ADMIN_ROLE_ID, cmd, resource_group_name, project_name, user_id)
