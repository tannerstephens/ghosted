from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .ghost_generator import GhostGenerator

cache = Cache()
migrate = Migrate()
db = SQLAlchemy()
ghost_generator = GhostGenerator()
