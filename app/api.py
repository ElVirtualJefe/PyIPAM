# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present ElVirtualJefe
"""

# Flask modules
from app.models.subnet import subnetModel
from flask   import Flask, request, render_template
from jinja2  import TemplateNotFound

# App modules
from app import app

# App main route + generic routing
#@app.route('/', defaults={'path': 'index'})
@app.route('/api/<path:path>')
def api(path):

    try:

        # Return JSON Response
        return {"response": "EMPTY"}
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

