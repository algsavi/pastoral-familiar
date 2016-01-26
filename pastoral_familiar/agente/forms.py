#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, HiddenField, BooleanField, DateField, PasswordField, SelectField, validators

class AgenteForm(Form):
    nome = TextField('Nome', [validators.Required(u'Você precisa digitar o nome!'),
                                    validators.Length(max=65)])
    dt_nascimento = DateField('Data Nascimento',
                            [validators.DataRequired(u'Você precisa digitar a data de nascimento!')],
                            format='%d/%m/%Y')

    celular = TextField('Celular', [validators.Length(max=15)])
    endereco = TextField(u'Endereço', [validators.DataRequired(u'Você precisa digitar o endereço!'), 
                                        validators.Length(max=125)])
    bairro = TextField(u'Bairro', [validators.DataRequired(u'Você precisa digitar o bairro!'), 
                                        validators.Length(max=30)])
    cep = TextField(u'CEP', [validators.DataRequired(u'Você precisa digitar o CEP!'), 
                                        validators.Length(max=10)])
    cidade = TextField('Cidade', [validators.DataRequired(u'Você precisa digitar a cidade!'),
                                    validators.Length(max=30)])
    telefone_residencial = TextField('Telefone Residencial', [validators.Length(max=15)])
    
    id_nucleo = SelectField(u'Núcleo', [validators.Required(u'Você precisa selecionar um núcleo')], coerce=int)


class AgenteFormEditar(AgenteForm):
    coordenador_nucleo = BooleanField(u'Coordenador Núcleo')

class AgenteFormInserir(AgenteForm):
    email = TextField('Email', [validators.DataRequired(u'Você precisa digitar o e-mail!'),
                                validators.Length(max=40), validators.email(u'E-mail inválido')])
    senha = PasswordField('Senha', [validators.DataRequired(u'Você precisa digitar a senha!'),
                                validators.Length(max=50)])

class LoginForm(Form):
    email = TextField('Email', [validators.DataRequired(u'Você precisa digitar o e-mail!'),
                                validators.Length(max=40), validators.email(u'E-mail inválido')])
    senha = PasswordField('Senha', [validators.DataRequired(u'Você precisa digitar a senha!'),
                                validators.Length(max=50)])
    remember_me = BooleanField('Lembrar acesso')