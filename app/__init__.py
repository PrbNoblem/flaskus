from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Config is defined such that the object passed to app above
# contains what is needed by SQLAlchemy to do its thing.
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# routes define the views, while models will define the structure of the database
from app import routes, models
