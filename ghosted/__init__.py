from flask import Flask
from flask_migrate import Migrate

def create_app(config='ghosted.config.Config'):
  app = Flask(__name__)

  app.config.from_object(config)

  with app.app_context():
    from .routes import register_routes
    register_routes(app)

    from .models import db
    Migrate(app, db)

  return app
