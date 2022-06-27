https://github.com/atlassian-api/atlassian-python-api
https://atlassian-python-api.readthedocs.io/

```
# To create a virtual environment in a given directory, type:
# python -m venv /path/to/directory
python3 -m venv venv

# Activate the virtual environment
. venv/bin/activate

pip install atlassian-python-api

# De-Activate the virtual environment
deactivate

# generate requirements.txt
pip3 freeze > requirements.txt

# recreate the virtual environment
pip install -r requirements.txt

```