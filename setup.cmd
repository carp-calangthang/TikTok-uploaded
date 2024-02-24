@echo off
set PYTHON_VERSION=3.11.0

echo Installing Python...
curl -L https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-embed-amd64.zip -o python.zip
mkdir python
tar -xf python.zip -C python --strip-components=1
set PATH=%CD%\python;%PATH%
del python.zip

echo Installing required libraries...
python -m pip install -r requirements.txt

echo Installation completed.
pause
