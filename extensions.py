#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import or_, and_
from flask.ext.login import LoginManager, login_required, current_user, login_user, logout_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, identity_changed, Identity, UserNeed

db = SQLAlchemy()
lm = LoginManager()
lm.login_view = 'agente.login'
lm.login_message = u'Por favor, faça o login para acessar a página!'