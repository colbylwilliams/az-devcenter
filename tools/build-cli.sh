#!/bin/bash

set -e

cdir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
tcdir=${cdir%/*}

echo "Azure CLI Build Utility"
echo ""

pushd $tcdir > /dev/null

    echo "Creating a virtual environment"
    python -m venv .venv
    echo ""

    echo "Activating virtual environment"
    source .venv/bin/activate
    echo ""

    echo "Installing Azure CLI Dev Tools (azdev)"
    pip install azdev
    echo ""

    echo "Setting up Azure CLI Dev Tools (azdev)"
    azdev setup -r $PWD -e dc
    echo ""

    echo "Running Linter on dc extension source"
    # azdev linter dc
    echo ""

    echo "Running Style Checks on dc extension source"
    azdev style dc
    echo ""

    echo "Building dc extension"
    azdev extension build dc --dist-dir ./release_assets
    echo ""

    echo "Deactivating virtual environment"
    deactivate
    echo ""

popd > /dev/null

echo "Done."
echo ""
