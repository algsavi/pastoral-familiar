#! /usr/bin/env python
# -*- coding: utf-8 -*-

from extensions import db

class Nucleo(db.Model):
    __tablename__ = 'nucleo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.VARCHAR(100))
    objetivo = db.Column(db.VARCHAR(300))