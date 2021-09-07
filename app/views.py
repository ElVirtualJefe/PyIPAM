# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from app.models.subnet import subnetModel
from flask   import Flask, request, render_template
from jinja2  import TemplateNotFound

# App modules
from app import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):

    try:

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path + ".html" )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

@app.route('/response', methods=['POST'])
def response():
    from app.models import db

    sname = request.form.get("sname")
    new_subnet = subnetModel(name=sname)
    db.session.add(new_subnet)
    db.session.commit()

    return f"Added {sname}!!"
    
@app.route('/<path:path>')
def catch_all(path):
    try:

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path + ".html" )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

