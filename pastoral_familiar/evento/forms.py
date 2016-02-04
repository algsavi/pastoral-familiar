#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, DecimalField, Field, DateField, SelectField, validators


class BRLDecimalField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            valuelist[0] = valuelist[0].replace('.', '') 
            valuelist[0] = valuelist[0].replace(',', '.') 
        return super(BRLDecimalField, self).process_formdata(valuelist)


class EventoForm(Form):
    descricao = TextField('Nome', [validators.Required(u'Você precisa digitar a descrição!'),
                                    validators.Length(max=100)])
    dt_evento = DateField('Data do Evento',
                            [validators.DataRequired(u'Você precisa digitar a data do evento!')],
                            format='%d/%m/%Y')
    tp_evento = SelectField(u'Tipo Evento', choices=[('', 'Selecione...'), ('E', 'Encontro'), ('F', u'Formação')], validators=[validators.Required(u'Você precisa selecionar o tipo do evento')])
    tx_inscricao = BRLDecimalField(u'Taxa Inscrição')
    id_nucleo = SelectField(u'Núcleo', [validators.Required(u'Você precisa selecionar um núcleo')], coerce=int)
