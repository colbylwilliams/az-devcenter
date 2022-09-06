# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

# from ._transformers import transform_rg_table


def load_command_table(self, _):  # pylint: disable=too-many-statements

    with self.command_group('dc', is_preview=True):
        pass

    with self.command_group('dc') as g:
        g.custom_command('upgrade', 'dc_upgrade')

    with self.command_group('dc project user') as g:
        g.custom_command('add', 'add_project_user')
        g.custom_command('remove', 'remove_project_user')

    with self.command_group('dc project admin') as g:
        g.custom_command('add', 'add_project_admin')
        g.custom_command('remove', 'remove_project_admin')
