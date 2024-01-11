
echo "Creating virtual environment for development in new directory."
.\ci\linux\create_venv.bat
echo "Updating dependencies"
.\ci\linux\update_dependencies.bat
echo "Installing dependencies"
.\ci\linux\install_dependencies.bat
