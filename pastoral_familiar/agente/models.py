#! /usr/bin/env python
# -*- coding: utf-8 -*-

from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Agente(db.Model):
    __tablename__ = 'agente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.VARCHAR(35))
    dt_nascimento = db.Column(db.Date)
    email = db.Column(db.VARCHAR(40))
    celular = db.Column(db.VARCHAR(15))
    endereco = db.Column(db.VARCHAR(65))
    cep = db.Column(db.VARCHAR(10))
    cidade = db.Column(db.VARCHAR(30))
    bairro = db.Column(db.VARCHAR(30))
    telefone_residencial = db.Column(db.VARCHAR(15))
    senha = db.Column(db.VARCHAR(250))
    coordenador_pastoral = db.Column(db.Boolean)
    coordenador_nucleo = db.Column(db.Boolean)
    ativo = db.Column(db.Boolean)
    id_nucleo = db.Column(db.Integer, db.ForeignKey('nucleo.id'))

    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)
    
    def is_active(self):
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return self.is_anonymous