#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, FieldList, HiddenField, DecimalField, Field, DateField, SelectField, validators


class InscricaoForm(Form):
    nome = FieldList(TextField('Nome', [validators.Length(max=65),
                                validators.Required(u'Você precisa digitar o nome!')]), min_entries=2)
    dt_nascimento = FieldList(DateField('Data Nascimento', [validators.Optional()],
                              format='%d/%m/%Y'), min_entries=2)
    celular = FieldList(TextField('Celular', [validators.Length(max=15),
                        validators.Required(u'Você precisa digitar o celular')]), min_entries=2)
    telefone_residencial = TextField('Telefone Residencial', [
                                     validators.Length(max=15), validators.Optional()])
    email = FieldList(TextField('Email', [validators.DataRequired(u'Você precisa digitar o e-mail!'),
                                validators.Length(max=40), validators.email(u'E-mail inválido')]), min_entries=2)
    rua = TextField(u'Rua', [validators.Optional(),
                             validators.Length(max=65)])
    numero = TextField(u'Número', [validators.Optional()])
    complemento = TextField(u'Complemento', [validators.Length(max=30), validators.Optional()])
    bairro = TextField(u'Bairro', [validators.Optional(),
                                   validators.Length(max=30)])
    cep = TextField(u'CEP', [validators.Optional(),
                             validators.Length(max=10)])
    cidade = TextField('Cidade', [validators.Optional(),
                                  validators.Length(max=30)])
    uf = TextField('UF', [validators.Optional(),
                          validators.Length(max=2)])
    dt_casamento = DateField('Data Casamento',
                              [validators.DataRequired(
                                  u'Você precisa digitar a data de casamento!')],
                              format='%d/%m/%Y')
    paroquia_casamento = TextField(u'Paróquia Casamento', [validators.Required(u'Você precisa digitar a Paróquia do Casamento'),
                            validators.Length(max=100)])  