FROM python:3.7
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD gunicorn --bind 0.0.0.0:80 -w 4 "ghosted:create_app()"
