# Resting

Resting is a simple boilerplate flask app.

## Getting Started

```bash

# get the source from the Git repository
git clone git@github.com:leesq/resting.git
cd resting

# set up the Python environment
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# create and initialise an SQLite database
python manage.py run_init_db

# start the application
python manage.py runserver

```