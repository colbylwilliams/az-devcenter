# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

# from knack.arguments import CLIArgumentType

from ._validators import dc_source_version_validator, user_validator


def load_arguments(self, _):
    with self.argument_context('dc upgrade') as c:
        c.argument('version', options_list=['--version', '-v'], help='Version (tag). Default: latest stable.',
                   validator=dc_source_version_validator)
        c.argument('prerelease', options_list=['--pre'], action='store_true',
                   help='Deploy latest prerelease version.')

    with self.argument_context('dc project') as c:
        # c.argument('dev_center', options_list=['--dev-center-name', '--dev-center', '-dc'], help='Project prefix.')
        c.argument('project_name', options_list=['--project-name', '--project', '-p'], help='Name of the project.')

    for scope in ['dc project user', 'dc project admin']:
        with self.argument_context(scope) as c:
            c.argument('user_id', options_list=['--user-id', '--user', '-u'], default='me', validator=user_validator,
                       help="The id of the user. If value is 'me', the identity is taken from the authentication "
                       "context.")
