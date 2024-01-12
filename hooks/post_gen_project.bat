
echo "Creating virtual environment for development in new directory."
.\ci\win32\create_venv.bat
echo "Updating dependencies"
.\ci\win32\update_dependencies.bat
echo "Installing dependencies"
.\ci\win32\install_dependencies.bat
