PIPENV_VENV_IN_PROJECT=1 /usr/local/bin/pipenv install
PIPENV_VENV_IN_PROJECT=1 FLASK_APP="ghosted:create_app()" /usr/local/bin/pipenv run flask db init
PIPENV_VENV_IN_PROJECT=1 FLASK_APP="ghosted:create_app()" /usr/local/bin/pipenv run flask db upgrade


sudo service ghosted restart
