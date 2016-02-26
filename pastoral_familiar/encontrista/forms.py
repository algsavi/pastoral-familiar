#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, FieldList, HiddenField, DecimalField, Field, DateField, SelectField, validators


class InscricaoForm(Form):
    nome = FieldList(TextField('Nome', [validators.Required(u'Você precisa digitar o nome!'),
                              validators.Length(max=65)]), min_entries=2)
    dt_nascimento = FieldList(DateField('Data Nascimento',
                              format='%d/%m/%Y'), min_entries=2)
    celular = FieldList(TextField('Celular', [validators.Length(max=15)]), min_entries=2)
    telefone_residencial = TextField('Telefone Residencial', [
                                     validators.Length(max=15)])
    email = FieldList(TextField('Email', [validators.DataRequired(u'Você precisa digitar o e-mail!'),
                                validators.Length(max=40), validators.email(u'E-mail inválido')]), min_entries=2)
    rua = TextField(u'Rua', [validators.Required(u'Você precisa digitar o endereço!'),
                             validators.Length(max=65)])
    numero = TextField(u'Número', [validators.Required(
        u'Você precisa digitar o número!')])
    complemento = TextField(u'Complemento', [validators.Length(max=30)])
    bairro = TextField(u'Bairro', [validators.Required(u'Você precisa digitar o bairro!'),
                                   validators.Length(max=30)])
    cep = TextField(u'CEP', [validators.DataRequired(u'Você precisa digitar o CEP!'),
                             validators.Length(max=10)])
    cidade = TextField('Cidade', [validators.DataRequired(u'Você precisa digitar a cidade!'),
                                  validators.Length(max=30)])
    uf = TextField('UF', [validators.DataRequired(u'Você precisa digitar o estado!'),
                          validators.Length(max=2)])
    dt_casamento = DateField('Data Casamento',
                              [validators.DataRequired(
                                  u'Você precisa digitar a data de casamento!')],
                              format='%d/%m/%Y')
    paroquia_casamento = TextField(u'Paróquia Casamento', [validators.Length(max=100)])  