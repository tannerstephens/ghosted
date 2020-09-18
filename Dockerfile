FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install
EXPOSE 80
RUN pipenv run flask db upgrade
ENTRYPOINT [ "pipenv" ]
CMD pipenv run gunicorn --bind 0.0.0.0:80 -w 4 "ghosted:create_app()"
