#! /usr/bin/env python
# -*- coding: utf-8 -*-

from extensions import db

class Evento(db.Model):
    __tablename__ = 'evento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.VARCHAR(100))
    dt_evento = db.Column(db.Date)
    tp_evento = db.Column(db.CHAR(1))
    tx_inscricao = db.Column(db.DECIMAL(7, 2))
    aberto_inscricao = db.Column(db.Boolean)
    id_nucleo = db.Column(db.Integer, db.ForeignKey('nucleo.id'))