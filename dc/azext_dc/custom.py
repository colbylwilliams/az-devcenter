# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.cli.core.util import is_guid
from knack.log import get_logger
# from knack.prompting import prompt_y_n
from knack.util import CLIError

from ._client_factory import devcenter_client_factory

logger = get_logger(__name__)

DEVBOX_USER_ROLE_ID = '45d50f46-0b78-4001-a660-4198cbe8cd05'
PROJECT_ADMIN_ROLE_ID = '331c37c6-af14-46d9-b9f4-e1909e1b95a0'


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


def add_project_user(cmd, resource_group_name, project_name, user_id='me'):
    return _add_project_role(DEVBOX_USER_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def add_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _add_project_role(PROJECT_ADMIN_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def _remove_project_role(role, cmd, resource_group_name, project_name, user_id='me'):
    from azure.cli.command_modules.role.custom import delete_role_assignments
    client = devcenter_client_factory(cmd.cli_ctx)
    project = client.projects.get(resource_group_name, project_name)

    if user_id.lower() == 'me':
        from azure.cli.core._profile import Profile
        user_id = Profile(cli_ctx=cmd.cli_ctx).get_current_account_user()

    return delete_role_assignments(cmd, role=role, assignee=user_id, scope=project.id)


def remove_project_user(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(DEVBOX_USER_ROLE_ID, cmd, resource_group_name, project_name, user_id)


def remove_project_admin(cmd, resource_group_name, project_name, user_id='me'):
    return _remove_project_role(PROJECT_ADMIN_ROLE_ID, cmd, resource_group_name, project_name, user_id)
