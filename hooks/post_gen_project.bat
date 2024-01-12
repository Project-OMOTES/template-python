
echo "Creating virtual environment for development in new directory."
call ci\win32\create_venv.cmd
echo "Updating dependencies"
call ci\win32\update_dependencies.cmd
echo "Installing dependencies"
call ci\win32\install_dependencies.cmd
