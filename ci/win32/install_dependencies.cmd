
pushd .
cd /D "%~dp0"
cd ..\..\
pip-sync .\dev-requirements.txt .\doc-requirements.txt .\requirements.txt
popd