from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar los modelos
from .User.user_models import User
from .Character.character_models import Character
from .Planet.planet_models import Planet
from .Favorite.favorite_models import Favorite