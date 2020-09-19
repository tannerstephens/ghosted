from .views import views
from .ghost_api import ghost_api

def register_routes(app):
  app.register_blueprint(views)
  app.register_blueprint(ghost_api)
