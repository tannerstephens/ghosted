from flask import Flask
from flask_migrate import Migrate

def create_app(config='ghosted.config.Config'):
  app = Flask(__name__)

  app.config.from_object(config)

  with app.app_context():
    from ghosted.views import views
    app.register_blueprint(views)


    from ghosted.models import db
    Migrate(app, db)

  return app
