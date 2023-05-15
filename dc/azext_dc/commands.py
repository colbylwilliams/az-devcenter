# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

# from ._transformers import transform_rg_table


def load_command_table(self, _):  # pylint: disable=too-many-statements

    with self.command_group('dc', is_preview=True):
        pass

    with self.command_group('dc') as g:
        g.custom_command('version', 'dc_version')
        g.custom_command('upgrade', 'dc_upgrade')
        # g.custom_command('test', 'dc_test')

    with self.command_group('dc devbox-user') as g:
        g.custom_command('check', 'dc_devbox_user_check')

    with self.command_group('dc box') as g:
        g.custom_command('list', 'list_dc_boxes')
        g.custom_command('start', 'start_dc_boxes')
        g.custom_command('stop', 'stop_dc_boxes')

    with self.command_group('dc project box') as g:
        g.custom_command('list', 'list_project_boxes')
        g.custom_command('start', 'start_project_boxes')
        g.custom_command('stop', 'stop_project_boxes')

    with self.command_group('dc project devbox-user') as g:
        g.custom_command('add', 'add_project_devbox_user')
        g.custom_command('remove', 'remove_project_devbox_user')
        g.custom_command('check', 'check_project_devbox_user')

    with self.command_group('dc project environments-user') as g:
        g.custom_command('add', 'add_project_environments_user')
        g.custom_command('remove', 'remove_project_environments_user')

    with self.command_group('dc project admin') as g:
        g.custom_command('add', 'add_project_admin')
        g.custom_command('remove', 'remove_project_admin')
