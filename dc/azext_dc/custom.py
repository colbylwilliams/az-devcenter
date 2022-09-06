# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.log import get_logger
# from knack.prompting import prompt_y_n
from knack.util import CLIError

from ._client_factory import resource_client_factory

logger = get_logger(__name__)


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
