# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint: disable=logging-fstring-interpolation

import json

from azure.cli.core.extension.operations import show_extension, update_extension
from azure.cli.core.util import is_guid
from azure.developer.devcenter.operations import DevBoxesOperations, DevCenterOperations, EnvironmentsOperations
from knack.log import get_logger
from knack.prompting import prompt_y_n
from knack.util import CLIError
from packaging.version import parse

from ._client_factory import (cf_dc_data, cf_dc_data_dev_boxes, cf_dc_data_dev_center, cf_dc_data_environments,
                              cf_dc_mgmt, get_graph_client)
from ._utils import get_github_latest_release_version, get_github_release

logger = get_logger(__name__)

ROLE_ID_DEVBOX_USER = '45d50f46-0b78-4001-a660-4198cbe8cd05'
ROLE_ID_PROJECT_ADMIN = '331c37c6-af14-46d9-b9f4-e1909e1b95a0'
ROLE_ID_ADE_USER = '18e40d4e-8d2e-438d-97e1-9528336e149c'

SERVICE_PLAN_ID_INTUNE_A = 'c1ec4a95-1f05-45b3-a911-aa3fa01094f5'
SERVICE_PLAN_ID_AAD_PREMIUM = '41781fb2-bc02-4b7c-bd55-b576c07bb09d'
SERVICE_PLAN_ID_WIN10_PRO_ENT_SUB = '21b439ba-a0ca-424f-a6cc-52f954a5b111'

# def dc_test(cmd, user='me'):
#     pass

# ----------------
# dc version
# dc upgrade
# ----------------


def dc_version(cmd):
    ext = show_extension('dc')
    current_version = 'v' + ext['version']
    is_dev = 'extensionType' in ext and ext['extensionType'] == 'dev'
    logger.info(f'Current version: {current_version}')
    current_version_parsed = parse(current_version)
    print(f'az dc version: {current_version}{" (dev)" if is_dev else ""}')

    latest_version = get_github_latest_release_version()
    logger.info(f'Latest version: {latest_version}')
    latest_version_parsed = parse(latest_version)

    if current_version_parsed < latest_version_parsed:
        logger.warning(f'There is a new version of az dc {latest_version}. Please update using: az dc upgrade')


def dc_upgrade(cmd, version=None, prerelease=False):
    ext = show_extension('dc')
    current_version = 'v' + ext['version']
    logger.info(f'Current version: {current_version}')
    current_version_parsed = parse(current_version)

    release = get_github_release(version=version, prerelease=prerelease)

    new_version = release['tag_name']
    logger.info(f'Latest{" prerelease" if prerelease else ""} version: {new_version}')
    new_version_parsed = parse(new_version)

    is_dev = 'extensionType' in ext and ext['extensionType'] == 'dev'

    if not is_dev and new_version_parsed == current_version_parsed:
        print(f'Already on latest{" prerelease" if prerelease else ""} version: {new_version}')
        return

    if not is_dev and new_version_parsed < current_version_parsed:
        print(f'Current version is newer than latest{" prerelease" if prerelease else ""} version: {new_version}')
        return

    logger.info(f'Upgrading to latest{" prerelease" if prerelease else ""} version: {new_version}')
    index = next((a for a in release['assets'] if 'index.json' in a['browser_download_url']), None)

    index_url = index['browser_download_url'] if index else None
    if not index_url:
        raise CLIError(f'Could not find index.json asset on release {new_version}. '
                       'Specify a specific prerelease version with --version/-v or use latest prerelease with --pre')

    if is_dev:
        logger.warning('Skipping upgrade of dev extension.')
        return

    update_extension(cmd, extension_name='dc', index_url=index_url)


# ----------------------------
# dc box
# ----------------------------


def _get_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None):  # pylint: disable=unused-argument
    # if user_ids and 'me' in user_ids:
    #     from azure.cli.core._profile import Profile
    #     user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()
    #     user_ids.remove('me')
    #     user_ids.append(user_id)

    client = cf_dc_data_dev_center(cmd.cli_ctx, dev_center)

    # get all projects in the devcenter
    logger.info(f'Getting projects in DevCenter: {dev_center} ...')
    projects = client.list_projects()
    projects = list(projects)

    # make sure we got a list of projects
    if not projects or len(projects) == 0:
        logger.warning(f'No projects found in devcenter: {dev_center}. Make sure you have at least Reader role on '
                       'the projects.')
        return []

    # filter projects by name (if specified)
    if project_names:
        projects = [p for p in projects if p['name'] in project_names]
        # ensure we have at least one project
        if len(projects) == 0:
            logger.error(f'No projects found in devcenter {dev_center} matching names: {project_names}. '
                         'Make sure you typed the names correctly and have at least Reader role on the projects.')
            return []
        # ensure we found all the projects we were looking for
        for name in project_names:
            if name not in [p['name'] for p in projects]:
                logger.error(f'No projects found in devcenter {dev_center} matching name: {name}. '
                             'Make sure you typed the name correctly and have at least Reader role on the project.')
                return []

    logger.info(f' found {len(projects)} {"project" if len(projects) == 1 else "projects"}: '
                f'{[n["name"] for n in projects]}')

    # would be ideal to create an odata query based in the projects/pools/users
    # but it doesn't look like the --filter argment is respected by the dataplane
    # get all dev-boxes in the devcenter
    all_boxes = client.list_all_dev_boxes()
    all_boxes = list(all_boxes)

    if not all_boxes or len(all_boxes) == 0:
        logger.warning(f'No boxes found in devcenter: {dev_center}. Make sure you have the DevCenter Project Admin '
                       'role on the projects.')
        return []

    return_boxes = []

    for project in projects:
        logger.info('')
        logger.info(f'Getting boxes in {project["name"]} ...')

        # filter boxes for the project
        project_boxes = [b for b in all_boxes if b["projectName"] == project["name"]]

        if not project_boxes or len(project_boxes) == 0:
            logger.warning(f'No boxes found in project: {project["name"]}. If this is incorrect, make sure you have the '
                           'DevCenter Project Admin role on the project.')
            continue

        # filter boxes by users (if specified)
        if user_ids:
            project_boxes = [b for b in project_boxes if b["user"] in user_ids]
            if len(project_boxes) == 0:
                logger.info(f' no boxes found matching users: {user_ids}')
                continue

        # filter boxes by pools (if specified)
        if pool_names:
            project_boxes = [b for b in project_boxes if b["poolName"] in pool_names]
            if len(project_boxes) == 0:
                logger.info(f' no boxes found matching pools: {pool_names}')
                continue

        corect_grammer = " matching specified pools/users" if user_ids or pool_names else ""
        logger.info(f' found {len(project_boxes)} {"box" if len(project_boxes) == 1 else "boxes"}{corect_grammer}: '
                    f'{[b["name"] for b in project_boxes]}')

        if len(project_boxes) > 0:
            return_boxes.extend(project_boxes)

    return return_boxes


def _start_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    boxes = _get_boxes(cmd, dev_center, project_names, pool_names, user_ids)

    not_deallocated = [b for b in boxes if b["powerState"].lower() != 'deallocated']
    if not_deallocated and len(not_deallocated) > 0:
        corect_grammer = "box because it isn't" if len(not_deallocated) == 1 else "boxes because they aren't"
        logger.info(f' skipping {len(not_deallocated)} {corect_grammer} deallocated: '
                    f'{[b["name"] for b in not_deallocated]}')

    # filter out boxes that are not deallocated
    boxes = [b for b in boxes if b["powerState"].lower() == 'deallocated']

    # if we still have boxes to start, start them
    if len(boxes) > 0:

        if not yes and not prompt_y_n(f'\nAre you sure you want to start {len(boxes)} boxes?', default='n'):
            return None

        db_client = cf_dc_data_dev_boxes(cmd.cli_ctx, dev_center)

        logger.info(f' starting {len(boxes)} {"box" if len(boxes) == 1 else "boxes"}')

        for box in boxes:
            logger.info(f' starting {box["name"]}...')
            db_client.begin_start_dev_box(box["projectName"], box["name"], user_id=box["user"])

    return _get_boxes(cmd, dev_center, project_names, pool_names, user_ids)


def _stop_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    boxes = _get_boxes(cmd, dev_center, project_names, pool_names, user_ids)

    not_running = [b for b in boxes if b["powerState"].lower() != 'running']
    if not_running and len(not_running) > 0:
        corect_grammer = "box because it isn't" if len(not_running) == 1 else "boxes because they aren't"
        logger.info(f' skipping {len(not_running)} {corect_grammer} running: {[b["name"] for b in not_running]}')

    # filter out boxes that are not running
    boxes = [b for b in boxes if b["powerState"].lower() == 'running']

    # if we still have boxes to stop, stop them
    if len(boxes) > 0:

        if not yes and not prompt_y_n(f'\nAre you sure you want to stop {len(boxes)} boxes?', default='n'):
            return None

        db_client = cf_dc_data_dev_boxes(cmd.cli_ctx, dev_center)

        logger.info(f' stopping {len(boxes)} {"box" if len(boxes) == 1 else "boxes"}')

        for box in boxes:
            logger.info(f' stopping {box["name"]}...')
            db_client.begin_stop_dev_box(box["projectName"], box["name"], user_id=box["user"])

    return _get_boxes(cmd, dev_center, project_names, pool_names, user_ids)


def list_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None):
    return _get_boxes(cmd, dev_center, project_names, pool_names, user_ids)


def start_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    return _start_boxes(cmd, dev_center, project_names, pool_names, user_ids, yes)


def stop_dc_boxes(cmd, dev_center, project_names=None, pool_names=None, user_ids=None, yes=False):
    return _stop_boxes(cmd, dev_center, project_names, pool_names, user_ids, yes)


def list_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None):
    return _get_boxes(cmd, dev_center, [project_name], pool_names, user_ids)


def start_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None, yes=False):
    return _start_boxes(cmd, dev_center, [project_name], pool_names, user_ids, yes)


def stop_project_boxes(cmd, dev_center, project_name, pool_names=None, user_ids=None, yes=False):
    return _stop_boxes(cmd, dev_center, [project_name], pool_names, user_ids, yes)


# ----------------------------
# dc project user
# ----------------------------

def _check_user_licenses(cmd, user):
    if user == 'me':
        from azure.cli.core._profile import Profile
        user = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()

    from azure.cli.command_modules.role.custom import _resolve_object_id

    try:
        user_id = _resolve_object_id(cmd.cli_ctx, user, fallback_to_object_id=True)

        client = get_graph_client(cmd.cli_ctx)
        result = client._send('GET', f'/users/{user_id}/licenseDetails')  # pylint: disable=protected-access

        service_plan_ids = []
        for license in result:
            service_plan_ids.extend([sp['servicePlanId'] for sp in license['servicePlans']])

        check_intune = SERVICE_PLAN_ID_INTUNE_A in service_plan_ids
        check_aad = SERVICE_PLAN_ID_AAD_PREMIUM in service_plan_ids
        check_win_sub = SERVICE_PLAN_ID_WIN10_PRO_ENT_SUB in service_plan_ids

        if check_intune and check_aad and check_win_sub:
            logger.info(f'{user} has valid licenses to use dev box')
            return (True, f'{user} has valid licenses to use dev box')

        logger.info(f'{user} does not have a valid license to use dev box')
        return (False, f'{user} does not have a valid license to use dev box')

    except Exception as ex:  # pylint: disable=broad-except
        logger.debug(ex)
        return (False, f'{ex}')


def _add_project_role(role, cmd, resource_group_name, project_name, user_id='me'):
    from azure.cli.command_modules.role.custom import create_role_assignment
    client = cf_dc_mgmt(cmd.cli_ctx)
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
    client = cf_dc_mgmt(cmd.cli_ctx)
    project = client.projects.get(resource_group_name, project_name)

    if user_id.lower() == 'me':
        from azure.cli.core._profile import Profile
        user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()

    return delete_role_assignments(cmd, role=role, assignee=user_id, scope=project.id)

# ----------------------------
# dc devbox-user
# ----------------------------


def dc_devbox_user_check(cmd, user_id='me'):
    check = _check_user_licenses(cmd, user_id)
    return check[1]


# ----------------------------
# dc project devbox-user
# ----------------------------

def add_project_devbox_user(cmd, resource_group_name, project_name, user_id='me', skip_license_check=False):
    if not skip_license_check:
        check = _check_user_licenses(cmd, user_id)
        if not check[0]:
            raise CLIError(check[1])

    return _add_project_role(ROLE_ID_DEVBOX_USER, cmd, resource_group_name, project_name, user_id)


def remove_project_devbox_user(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(ROLE_ID_DEVBOX_USER, cmd, resource_group_name, project_name, user_id)


# ----------------------------
# dc project environments-user
# ----------------------------

def add_project_environments_user(cmd, resource_group_name, project_name, user_id='me', skip_license_check=False):
    if not skip_license_check:
        check = _check_user_licenses(cmd, user_id)
        if not check[0]:
            raise CLIError(check[1])

    return _add_project_role(ROLE_ID_ADE_USER, cmd, resource_group_name, project_name, user_id)


def remove_project_environments_user(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(ROLE_ID_ADE_USER, cmd, resource_group_name, project_name, user_id)


# ----------------------------
# dc project admin
# ----------------------------


def add_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _add_project_role(ROLE_ID_PROJECT_ADMIN, cmd, resource_group_name, project_name, user_id)


def remove_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(ROLE_ID_PROJECT_ADMIN, cmd, resource_group_name, project_name, user_id)
