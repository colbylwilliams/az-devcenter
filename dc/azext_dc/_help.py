# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# ----------------
# dc
# ----------------

helps['dc'] = """
type: group
short-summary: Utilities for common or DevCenter tasks.
"""

helps['dc upgrade'] = """
type: command
short-summary: Update dc cli extension.
examples:
  - name: Update dc cli extension.
    text: az dc upgrade
  - name: Update dc cli extension to the latest pre-release.
    text: az dc upgrade --pre
"""
