# Steps for installing virtual environment
python3 -m venv .venv 
source .venv/bin/activate
pip install --upgrade pip
# pip install wheel
# python3 setup.py bdist_wheel sdist
pip install .
# pip install -r requirements.txt

# How to activate virtual environment
source .venv/bin/activate  # Linux

# How to deactivate virtual environment
deactivate
