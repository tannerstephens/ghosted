from flask import Flask
from .routes import register_routes
from .extensions import (
  migrate,
  db,
  ghost_generator
)

def create_app(config='ghosted.config.Config'):
  app = Flask(__name__)

  app.config.from_object(config)

  register_extensions(app)
  register_routes(app)

  return app


def register_extensions(app):
  db.init_app(app)
  migrate.init_app(app)
  ghost_generator.init_app(app)
