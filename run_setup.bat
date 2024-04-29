REM Steps for installing virtual environment and package on Windows
python -m venv .venv 
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
REM python -m pip install wheel
REM #python setup.py bdist_wheel sdist
python -m pip install .
REM python -m pip install -r requirements.txt

REM How to activate virtual environment
call .venv\Scripts\activate.bat

REM How to deactivate virtual environment
deactivate
