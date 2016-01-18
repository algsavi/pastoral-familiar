#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from .nucleo.views import nucleo
from .agente.views import agente
from extensions import db

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(agente, url_prefix='/agente')
app.register_blueprint(nucleo, url_prefix='/nucleo')

db.init_app(app)