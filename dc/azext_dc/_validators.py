# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from re import match

from azure.cli.core.util import CLIError
from knack.log import get_logger

logger = get_logger(__name__)


def prefix_validator(cmd, ns):
    if not ns.prefix:
        raise CLIError('--prefix|-p must be a valid string')


def dc_source_version_validator(cmd, ns):
    if ns.version:
        if ns.prerelease:
            raise CLIError(
                'usage error: can only use one of --version/-v | --pre')
        ns.version = ns.version.lower()
        if ns.version[:1].isdigit():
            ns.version = 'v' + ns.version
        if not _is_valid_version(ns.version):
            raise CLIError(
                '--version/-v should be in format v0.0.0 do not include -pre suffix')

        from ._utils import github_release_version_exists

        if not github_release_version_exists(ns.version):
            raise CLIError(f'--version/-v {ns.version} does not exist')


def _is_valid_url(url):
    return match(
        r'^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$', url) is not None


def _is_valid_version(version):
    return match(r'^v[0-9]+\.[0-9]+\.[0-9]+$', version) is not None
