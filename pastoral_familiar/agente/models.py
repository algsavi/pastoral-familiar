#! /usr/bin/env python
# -*- coding: utf-8 -*-

from extensions import db
from flask_security import UserMixin, RoleMixin

perfis_agentes = db.Table('perfis_agentes',
        db.Column('id_agente', db.Integer(), db.ForeignKey('agente.id')),
        db.Column('id_perfil', db.Integer(), db.ForeignKey('perfil.id')))

class Agente(UserMixin, db.Model):
    __tablename__ = 'agente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.VARCHAR(65))
    dt_nascimento = db.Column(db.Date)
    email = db.Column(db.VARCHAR(40))
    celular = db.Column(db.VARCHAR(15))
    rua = db.Column(db.VARCHAR(65))
    cep = db.Column(db.VARCHAR(10))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.VARCHAR(50))
    cidade = db.Column(db.VARCHAR(30))
    bairro = db.Column(db.VARCHAR(30))
    uf = db.Column(db.VARCHAR(2))
    telefone_residencial = db.Column(db.VARCHAR(15))
    password = db.Column(db.VARCHAR(250))
    coordenador_pastoral = db.Column(db.Boolean)
    coordenador_nucleo = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    id_nucleo = db.Column(db.Integer, db.ForeignKey('nucleo.id'))
    roles = db.relationship('Perfil', secondary=perfis_agentes, backref='perfil', lazy='dynamic')

    #def define_senha(self, senha):
    #    self.senha = generate_password_hash(senha)

    #def verifica_senha(self, senha):
    #    return check_password_hash(self.senha, senha)

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return self.is_anonymous


class Perfil(RoleMixin, db.Model):
    __tablename__ = 'perfil'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(35))
    description = db.Column(db.VARCHAR(100))