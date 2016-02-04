#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, HiddenField, BooleanField, DateField, PasswordField, SelectField, validators
from flask.ext.security.forms import LoginForm, ChangePasswordForm, RegisterForm
from flask.ext.security.utils import encrypt_password
from models import Agente


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
    password = PasswordField('Senha', [validators.DataRequired(u'Você precisa digitar a senha!'),
                                validators.Length(max=50),
                                validators.EqualTo('password_confirm', message='As senhas precisam ser as mesmas!')])
    
    password_confirm = PasswordField('Conformar Senha', [validators.DataRequired(u'Você precisa digitar a senha!'),
                                validators.Length(max=50)])


def validaLogin(email):
    agente = Agente.query.filter(Agente.email==email.data).first()

    if agente is not None:
        return agente

class PFLoginForm(LoginForm):
    email = TextField('Email', [validators.DataRequired(u'Você precisa digitar o e-mail!'),
                                validators.Length(max=40), validators.email(u'E-mail inválido')])
    password = PasswordField('Senha', [validators.DataRequired(u'Você precisa digitar a senha!'),
                                validators.Length(max=50)])
    remember = BooleanField('Lembrar acesso')

    def validate(self):
        self.user = validaLogin(self.email)

        if self.user and self.user.password.startswith("pbkdf2:sha1"):
            if check_password_hash(self.user.password, self.password.data):
                self.user.password = encrypt_password(self.password.data)
                
                return True 
        
        if not super(PFLoginForm, self).validate():
            return False

        return True


class AlterarSenhaForm(ChangePasswordForm):
    password = PasswordField('Senha', [validators.DataRequired(u'Você precisa digitar a senha atual!'),
                                validators.Length(max=50)])
    new_password = PasswordField('Nova Senha', [validators.DataRequired(u'Você precisa digitar a nova senha!'),
                                validators.Length(max=50),
                                validators.EqualTo('new_password_confirm', message='As senhas precisam ser as mesmas!')])

    new_password_confirm = PasswordField('Confirmar Senha', [validators.DataRequired(u'Você precisa confirmar a senha!'),
                                validators.Length(max=50)])