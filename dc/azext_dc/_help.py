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

# ----------------
# dc project
# ----------------

helps['dc project'] = """
type: group
short-summary: Manage projects.
"""

# ----------------
# dc project user
# ----------------

helps['dc project user'] = """
type: group
short-summary: Manage project devbox users.
"""

helps['dc project user add'] = """
type: command
short-summary: Add a DevBox User to a project.
examples:
  - name: Add a DevBox User to a project.
    text: az dc project user add -g ProjectRG -p MyProject -u me
"""

helps['dc project user remove'] = """
type: command
short-summary: Remove a DevBox User from a project.
examples:
  - name: Remove a DevBox User from a project.
    text: az dc project user remove -g ProjectRG -p MyProject -u me
"""

# ----------------
# dc project admin
# ----------------

helps['dc project admin'] = """
type: group
short-summary: Manage project admins.
"""

helps['dc project admin add'] = """
type: command
short-summary: Add a Project Admin to a project.
examples:
  - name: Add a Project Admin to a project.
    text: az dc project admin add -g ProjectRG -p MyProject -u me
"""

helps['dc project admin remove'] = """
type: command
short-summary: Remove a Project Admin from a project.
examples:
  - name: Remove a Project Admin from a project.
    text: az dc project admin remove -g ProjectRG -p MyProject -u me
"""
