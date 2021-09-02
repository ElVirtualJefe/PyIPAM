#app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

# initialize our db
db = SQLAlchemy(app)
migrate = Migrate(app,db)
