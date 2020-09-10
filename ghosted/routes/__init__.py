from .views import views

def register_routes(app):
  app.register_blueprint(views)
