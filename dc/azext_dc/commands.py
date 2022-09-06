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
