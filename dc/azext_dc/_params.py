# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.arguments import CLIArgumentType

from ._validators import dc_source_version_validator, prefix_validator


def load_arguments(self, _):
    with self.argument_context('dc upgrade') as c:
        c.argument('version', options_list=['--version', '-v'], help='Version (tag). Default: latest stable.',
                   validator=dc_source_version_validator)
        c.argument('prerelease', options_list=['--pre'], action='store_true',
                   help='Deploy latest prerelease version.')

    with self.argument_context('dc project') as c:
        c.argument('devcenter', options_list=['--dev-center-name', '--dev-center', '-dc'], help='Project prefix.')
        c.argument('project', options_list=['--project-nam', '--project', '-p'], help='Name of the project.')

    with self.argument_context('dc project user add') as c:
        c.argument('user', options_list=['--user-id', '--user', '-u'], default='me',
                   help="The id of the user. If value is 'me', the identity is taken from the authentication context.")
