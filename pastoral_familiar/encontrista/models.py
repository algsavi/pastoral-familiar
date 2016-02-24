#! /usr/bin/env python
# -*- coding: utf-8 -*-

from extensions import db


class Encontrista(db.Model):
    __tablename__ = 'encontrista'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.VARCHAR(65))
    dt_nascimento = db.Column(db.Date)
    email = db.Column(db.VARCHAR(40))
    celular = db.Column(db.VARCHAR(15))
    sexo = db.Column(db.CHAR(1))


class CasalEncontrista(db.Model):
    __tablename__ = 'casal_encontrista'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.VARCHAR(65))
    cep = db.Column(db.VARCHAR(10))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.VARCHAR(50))
    cidade = db.Column(db.VARCHAR(30))
    bairro = db.Column(db.VARCHAR(30))
    uf = db.Column(db.VARCHAR(2))
    telefone_residencial = db.Column(db.VARCHAR(15))
    dt_casamento = db.Column(db.Date)
    paroquia_casamento = db.Column(db.VARCHAR())
    id_encontro = db.Column(db.Integer, db.ForeignKey('evento.id'))
    id_esposa = db.Column(db.Integer, db.ForeignKey('encontrista.id'))
    id_esposo = db.Column(db.Integer, db.ForeignKey('encontrista.id'))