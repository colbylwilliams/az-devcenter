# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from pathlib import Path
from re import search

path_root = Path(__file__).resolve().parent.parent
path_dc = path_root / 'dc'

with open(path_dc / 'setup.py', 'r') as f:
    for line in f:
        if line.startswith('VERSION'):
            txt = str(line).rstrip()
            match = search(r'VERSION = [\'\"](.*)[\'\"]$', txt)
            if match:
                print("::set-output name=version::{}".format(match.group(1)))
