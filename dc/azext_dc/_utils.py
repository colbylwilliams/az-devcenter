# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import requests

from azure.cli.core.azclierror import ClientRequestError, MutuallyExclusiveArgumentError, ResourceNotFoundError
from azure.cli.core.util import should_disable_connection_verify
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


# def get_github_release(repo='az-devcenter', org='colbylwilliams', version=None, prerelease=False):

#     if version and prerelease:
#         raise CLIError(
#             'usage error: can only use one of --version/-v | --pre')

#     url = f'https://api.github.com/repos/{org}/{repo}/releases'

#     if prerelease:
#         version_res = requests.get(url, verify=not should_disable_connection_verify())
#         version_json = version_res.json()

#         version_prerelease = next((v for v in version_json if v['prerelease']), None)
#         if not version_prerelease:
#             raise CLIError(f'--pre no prerelease versions found for {org}/{repo}')

#         return version_prerelease

#     url += (f'/tags/{version}' if version else '/latest')

#     version_res = requests.get(url, verify=not should_disable_connection_verify())

#     if version_res.status_code == 404:
#         raise CLIError(
#             f'No release version exists for {org}/{repo}. '
#             'Specify a specific prerelease version with --version '
#             'or use latest prerelease with --pre')

#     return version_res.json()


# def github_release_version_exists(version, repo='az-devcenter', org='colbylwilliams'):

#     version_url = f'https://api.github.com/repos/{org}/{repo}/releases/tags/{version}'
#     version_res = requests.get(version_url, verify=not should_disable_connection_verify())

#     return version_res.status_code < 400


def get_github_releases(org='colbylwilliams', repo='az-devcenter', prerelease=False):
    url = f'https://api.github.com/repos/{org}/{repo}/releases'

    version_res = requests.get(url, verify=not should_disable_connection_verify())
    version_json = version_res.json()

    return [v for v in version_json if v['prerelease'] == prerelease]


def get_github_release(org='colbylwilliams', repo='az-devcenter', version=None, prerelease=False):
    if version and prerelease:
        raise MutuallyExclusiveArgumentError('Only use one of --version/-v | --pre')

    url = f'https://api.github.com/repos/{org}/{repo}/releases'

    if prerelease:
        if (prereleases := get_github_releases(org, repo, prerelease=True)):
            return prereleases[0]
        raise ClientRequestError(f'--pre no prerelease versions found for {org}/{repo}')

    url += (f'/tags/{version}' if version else '/latest')

    version_res = requests.get(url, verify=not should_disable_connection_verify())

    if version_res.status_code == 404:
        raise ClientRequestError(
            f'No release version exists for {org}/{repo}. Specify a specific prerelease version with --version '
            'or use latest prerelease with --pre')

    return version_res.json()


def get_github_latest_release_version(org='colbylwilliams', repo='az-devcenter', prerelease=False):
    logger.info(f'Getting latest release version from GitHub ({org}/{repo})')
    version_json = get_github_release(org, repo, prerelease=prerelease)
    return version_json['tag_name']


def github_release_version_exists(version, org='colbylwilliams', repo='az-devcenter'):
    logger.info(f'Checking if release version {version} exists on GitHub ({org}/{repo})')
    version_url = f'https://api.github.com/repos/{org}/{repo}/releases/tags/{version}'
    version_res = requests.get(version_url, verify=not should_disable_connection_verify())
    return version_res.status_code < 400
