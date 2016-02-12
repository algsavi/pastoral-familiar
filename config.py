#! /usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = 'XIkJIUYjJLKWQq0921'

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mko09xsw23@localhost/pastoral_familiar"
SQLALCHEMY_POOL_SIZE = 5

DATA_PER_PAGE = 10

SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_REGISTERABLE = False
SECURITY_URL_PREFIX = '/agente'
SECURITY_CHANGE_URL = '/trocar_senha'
SECURITY_RESET_URL = '/reset_senha'
SECURITY_LOGIN_URL = '/login'
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = 'Instruções para definição de nova senha'
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = 'Sua senha foi alterada'
SECURITY_POST_LOGIN_VIEW = 'agente'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = '6e95b1ed-a8c3-4da0-8bac-6fcb11c39ab4'
SECURITY_MSG_INVALID_PASSWORD = (u'Senha inválida', 'danger')
SECURITY_MSG_USER_DOES_NOT_EXIST = (u'Usuário inválido', 'danger')
SECURITY_MSG_PASSWORD_NOT_PROVIDED = (u"Senha não fornecida", "danger")
SECURITY_MSG_EMAIL_NOT_PROVIDED = (u"E-mail não fornecido", "danger")
SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = (u"As senhas não conferem", "danger")
SECURITY_MSG_PASSWORD_IS_THE_SAME = (u"A nova senha precisa ser diferente da senha anterior", "danger")
SECURITY_MSG_LOGIN = (u"Por favor, faça o login para acessar a página", "danger")
SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = (u"Token inválido", "danger")
SECURITY_MSG_PASSWORD_RESET = (u'Sua senha foi redefinida com sucesso.', 'success')
SECURITY_MSG_PASSWORD_CHANGE = (u'Sua senha foi alterada com sucesso.', 'success')
SECURITY_MSG_PASSWORD_RESET_REQUEST = (u'As instruções para alterar sua senha foram enviadas para o seu e-mail.', 'success')

MAIL_SERVER = '50.56.21.178'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'postmaster@pastoralfamiliarsagradafamilia.com'
MAIL_PASSWORD = 'mko09xsw23'