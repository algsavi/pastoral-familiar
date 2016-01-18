#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, validators

class NucleoForm(Form):
    descricao = TextField(u'Descrição', [validators.Required(u'Você precisa digitar a descrição!'),
									validators.Length(max=100)])
    objetivo = TextField('Objetivo', [validators.Length(max=100)])