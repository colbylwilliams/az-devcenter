# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.arguments import CLIArgumentType

from ._validators import dc_source_version_validator, user_validator


def load_arguments(self, _):

    confirm_type = CLIArgumentType(
        help='Do not prompt for confirmation. WARNING: This is irreversible.',
        action='store_true',
        required=False,
        options_list=['--yes', '-y']
    )

    with self.argument_context('dc upgrade') as c:
        c.argument('version', options_list=['--version', '-v'], help='Version (tag). Default: latest stable.',
                   validator=dc_source_version_validator)
        c.argument('prerelease', options_list=['--pre'], action='store_true',
                   help="The id of the user. If value is 'me', the identity is taken from the authentication "
                   'context.')

    with self.argument_context('dc box') as c:
        c.argument('project_names', options_list=['--projects'], nargs='*',
                   help='Space-separated Project names to include. If not specified, all projects are included.')

    for scope in ['dc box', 'dc project box']:
        with self.argument_context(scope) as c:
            c.argument('dev_center', options_list=['--dev-center', '-dc'], help='Dev Center name.')
            c.argument('pool_names', options_list=['--pools'], nargs='*',
                       help='Space-separated Pool names to include. If not specified, all pools are included.')
            c.argument('user_ids', options_list=['--users'], nargs='*',
                       help='Space-separated user ids to include. If not specified, all users are included.')

    for scope in ['dc box stop', 'dc box start', 'dc project box stop', 'dc project box start']:
        with self.argument_context(scope) as c:
            c.argument('yes', arg_type=confirm_type)

    with self.argument_context('dc project') as c:
        # c.argument('dev_center', options_list=['--dev-center-name', '--dev-center', '-dc'], help='Project prefix.')
        c.argument('project_name', options_list=['--project-name', '--project', '-p'], help='Name of the project.')

    for scope in ['dc devbox-user check', 'dc project devbox-user', 'dc project environments-user', 'dc project admin']:
        with self.argument_context(scope) as c:
            c.argument('user_id', options_list=['--user-id', '--user', '-u'], default='me', validator=user_validator,
                       help="The id of the user. If value is 'me', the identity is taken from the authentication "
                       'context.')

    for scope in ['dc project devbox-user add', 'dc project environments-user add']:
        with self.argument_context(scope) as c:
            c.argument('skip_license_check', options_list=['--skip-license-check'], action='store_true',
                       help='Skip license check.')
