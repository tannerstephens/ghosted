from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .ghost_generator import GhostGenerator

migrate = Migrate()
db = SQLAlchemy()
ghost_generator = GhostGenerator()
