[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19613410&assignment_repo_type=AssignmentRepo)
# Movie review website

This codebase implements a simple movie review website written in Python and Django.

# Setup

To setup the basic website you will need to have the following installed:

- python3
- pip
- sqlite3

Pip is the package manager for Python.  You can install the remaining packages required for this task using pip. You will need to run the following:
To start you should create and activate a virtual environment:

- $ python -m venv env        # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
- $ source env/bin/activate   # use `env\Scripts\activate` on Windows
- $ pip install -r requirements.txt

You then need to apply the migrations by typing:

 $ python manage.py migrate

# Intialising the database

To initialise the database, next run:

 $ python manage.py loaddata db_initialisation.json

# Run the website

You can run the website by typing:

 $ python manage.py runserver

You can now browse to the url http://127.0.0.1:8000/ to view the website.


