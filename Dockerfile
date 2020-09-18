FROM python:3.7
RUN pip install pipenv
RUN pipenv install
CMD pipenv run gunicorn --bind 0.0.0.0:80 -w 4 "ghosted:create_app()"
