REM Steps for installing virtual environment on Windows
python -m venv .venv 
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM How to activate virtual environment
call .venv\Scripts\activate.bat

REM How to deactivate virtual environment
deactivate
