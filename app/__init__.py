# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# import Flask 
from flask import Flask
from urllib.parse import quote_plus as urlquote

# Inject Flask magic
app = Flask(__name__)

import os;
env = os.getenv('FLASK_ENV')

# App Config - the minimal footprint
#app.config.from_object("config.DevelopmentConfig")
if (env == "development"):
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")
app.config['TESTING'   ] = True 
app.config['SECRET_KEY'] = 'S#perS3crEt_JamesBond' 
# our database uri
username = app.config["DB_USERNAME"]
password = urlquote(app.config["DB_PASSWORD"])
dbname = app.config["DB_NAME"]
dbserver = app.config["DB_SERVER"]
dbport = app.config["DB_PORT"]

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{dbserver}:{dbport}/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Import routing to render the pages
from app import views

from app.models import db
#from sqlalchemy import create_engine
from app.models import *

#engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
db.create_all()


