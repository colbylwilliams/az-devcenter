# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType

from ._help import helps  # pylint: disable=unused-import
from ._params import load_arguments
from .commands import load_command_table


class DcCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        dc_custom = CliCommandType(
            operations_tmpl='azext_dc.custom#{}')
        super().__init__(cli_ctx=cli_ctx, custom_command_type=dc_custom)

    def load_command_table(self, args):
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        load_arguments(self, command)


COMMAND_LOADER_CLS = DcCommandsLoader
