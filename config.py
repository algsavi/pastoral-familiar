#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
SECURITY_POST_LOGIN_VIEW = 'agente'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = '6e95b1ed-a8c3-4da0-8bac-6fcb11c39ab4'
SECURITY_MSG_INVALID_PASSWORD = (u'Senha inválida', 'error')
SECURITY_MSG_USER_DOES_NOT_EXIST = (u'Usuário inválido', 'error')
SECURITY_MSG_PASSWORD_NOT_PROVIDED = (u"Senha não fornecida", "error")
SECURITY_MSG_EMAIL_NOT_PROVIDED = (u"E-mail não fornecido", "error")
SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = (u"As senhas não conferem", "error")
SECURITY_MSG_PASSWORD_IS_THE_SAME = (u"A nova senha precisa ser diferente da senha anterior", "error")
SECURITY_MSG_LOGIN = (u"Por favor, faça o login para acessar a página", "error")
SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = (u"Token inválido", "error")

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'postmaster@pastoralfamiliarsagradafamilia.com'
MAIL_PASSWORD = 'mko09xsw23'