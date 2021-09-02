# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# import Flask 
from flask import Flask
from urllib.parse import quote_plus as urlquote

# Inject Flask magic
app = Flask(__name__)

# App Config - the minimal footprint
app.config['TESTING'   ] = True 
app.config['SECRET_KEY'] = 'S#perS3crEt_JamesBond' 
# our database uri
username = "postgres"
password = urlquote("PyIPAM-P@ssw0rd123!")
dbname = "PyIPAM"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Import routing to render the pages
from app import views

from app.models import db
from sqlalchemy import create_engine

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
db.create_all(engine)

