# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

# ----------------------------
# dc
# ----------------------------

helps['dc'] = """
type: group
short-summary: Utilities for common or dev center tasks.
"""

helps['dc version'] = """
type: command
short-summary: Show the version of the dc extension.
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

# ----------------------------
# dc devbox-user
# ----------------------------

helps['dc devbox-user'] = """
type: group
short-summary: Manage dev box users.
"""

helps['dc devbox-user check'] = """
type: command
short-summary: Check if a user has appropriate licenses to use dev box.
examples:
  - name: Check if a user has appropriate licenses to use dev box.
    text: az dc devbox-user check --user user@example.com
"""

# ----------------------------
# dc box
# ----------------------------

helps['dc box'] = """
type: group
short-summary: Manage dev boxes.
"""

helps['dc box list'] = """
type: command
short-summary: List dev boxes.
examples:
  - name: List all dev boxes in a dev center.
    text: az dc box list -dc MyDevCenter
  - name: List all dev boxes in a specific project in a dev center.
    text: az dc box list -dc MyDevCenter --projects MyProject
  - name: List all dev boxes in a dev center belonging to specific users.
    text: az dc box list -dc MyDevCenter --users userA userB
"""

helps['dc box start'] = """
type: command
short-summary: Start dev boxes.
examples:
  - name: Start all dev boxes in a dev center.
    text: az dc box start -dc MyDevCenter
  - name: Start all dev boxes in a specific project in a dev center.
    text: az dc box start -dc MyDevCenter --projects MyProject
  - name: Start all dev boxes in a dev center belonging to specific users.
    text: az dc box start -dc MyDevCenter --users userA userB
"""

helps['dc box stop'] = """
type: command
short-summary: Stop dev boxes.
examples:
  - name: Stop all dev boxes in a dev center.
    text: az dc box stop -dc MyDevCenter
  - name: Stop all dev boxes in a specific project in a dev center.
    text: az dc box stop -dc MyDevCenter --projects MyProject
  - name: Stop all dev boxes in a dev center belonging to specific users.
    text: az dc box stop -dc MyDevCenter --users userA userB
"""

# ----------------------------
# dc project
# ----------------------------

helps['dc project'] = """
type: group
short-summary: Manage projects.
"""

# ----------------------------
# dc project box
# ----------------------------


helps['dc project box'] = """
type: group
short-summary: Manage project dev boxes.
"""

helps['dc project box list'] = """
type: command
short-summary: List project dev boxes.
examples:
  - name: List all dev boxes in a project.
    text: az dc project box list -dc MyDevCenter -p MyProject
  - name: List all dev boxes in specific pools in a project.
    text: az dc project box list -dc MyDevCenter -p MyProject --pools poolA poolB
  - name: List all dev boxes in a project belonging to specific users.
    text: az dc project box list -dc MyDevCenter -p MyProject --users userA userB
"""

helps['dc project box start'] = """
type: command
short-summary: Start project dev boxes.
examples:
  - name: Start all dev boxes in a project.
    text: az dc project box start -dc MyDevCenter -p MyProject
  - name: Start all dev boxes in specific pools in a project.
    text: az dc project box start -dc MyDevCenter -p MyProject --pools poolA poolB
  - name: Start all dev boxes in a project belonging to specific users.
    text: az dc project box start -dc MyDevCenter -p MyProject --users userA userB
"""

helps['dc project box stop'] = """
type: command
short-summary: Stop project dev boxes.
examples:
  - name: Stop all dev boxes in a project.
    text: az dc project box stop -dc MyDevCenter -p MyProject
  - name: Stop all dev boxes in specific pools in a project.
    text: az dc project box stop -dc MyDevCenter -p MyProject --pools poolA poolB
  - name: Stop all dev boxes in a project belonging to specific users.
    text: az dc project box stop -dc MyDevCenter -p MyProject --users userA userB
"""


# ----------------------------
# dc project devbox-user
# ----------------------------

helps['dc project devbox-user'] = """
type: group
short-summary: Manage project dev box users.
"""

helps['dc project devbox-user add'] = """
type: command
short-summary: Add a dev box user to a project.
examples:
  - name: Add a dev box user to a project.
    text: az dc project devbox-user add -g projectRG -p MyProject -u me
"""

helps['dc project devbox-user remove'] = """
type: command
short-summary: Remove a dev box user from a project.
examples:
  - name: Remove a dev box user from a project.
    text: az dc project devbox-user remove -g projectRG -p MyProject -u me
"""


# ----------------------------
# dc project environments-user
# ----------------------------

helps['dc project environments-user'] = """
type: group
short-summary: Manage project azure deployment environments users.
"""

helps['dc project environments-user add'] = """
type: command
short-summary: Add an azure deployment environments user to a project.
examples:
  - name: Add an azure deployment environments user to a project.
    text: az dc project environments-user add -g projectRG -p MyProject -u me
"""

helps['dc project environments-user remove'] = """
type: command
short-summary: Remove an azure deployment environments user from a project.
examples:
  - name: Remove an azure deployment environments user from a project.
    text: az dc project environments-user remove -g projectRG -p MyProject -u me
"""


# ----------------------------
# dc project admin
# ----------------------------

helps['dc project admin'] = """
type: group
short-summary: Manage project admins.
"""

helps['dc project admin add'] = """
type: command
short-summary: Add a project admin to a project.
examples:
  - name: Add a project admin to a project.
    text: az dc project admin add -g projectRG -p MyProject -u me
"""

helps['dc project admin remove'] = """
type: command
short-summary: Remove a project admin from a project.
examples:
  - name: Remove a project admin from a project.
    text: az dc project admin remove -g projectRG -p MyProject -u me
"""
