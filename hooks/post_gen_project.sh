#!/bin/bash

echo "Creating virtual environment for development in new directory."
ci/linux/create_venv.sh
echo "Updating dependencies"
ci/linux/update_dependencies.sh
echo "Installing dependencies"
ci/linux/install_dependencies.sh
