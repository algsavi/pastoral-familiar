#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, render_template, redirect, url_for, g
from .nucleo.views import nucleo
from .agente.views import agente
from .evento.views import evento
from .encontrista.views import encontrista
from extensions import db  
from .agente.models import Agente, Perfil
from .agente.forms import PFLoginForm, AlterarSenhaForm, AgenteForm
from flask.ext.security import SQLAlchemyUserDatastore, current_user, Security
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(agente, url_prefix='/agente')
app.register_blueprint(nucleo, url_prefix='/nucleo')
app.register_blueprint(evento, url_prefix='/evento')
app.register_blueprint(encontrista, url_prefix='/encontrista')

db.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, Agente, Perfil)
security = Security(app, user_datastore, login_form=PFLoginForm,
                        change_password_form=AlterarSenhaForm,
                        register_form=AgenteForm)

mail = Mail(app)
Bootstrap(app)

@app.route('/')
def app_redirect():
    return redirect(url_for('agente.index'))

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.user = current_user