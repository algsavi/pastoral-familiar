#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, render_template, redirect, url_for
from .nucleo.views import nucleo
from .agente.views import agente
from extensions import db, lm, Principal, identity_loaded, Identity, UserNeed, RoleNeed

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(agente, url_prefix='/agente')
app.register_blueprint(nucleo, url_prefix='/nucleo')

db.init_app(app)
lm.init_app(app)
principals = Principal(app)

@app.route('/')
def app_redirect():
    return redirect(url_for('agente.index'))

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404