#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Blueprint, render_template, request, flash, redirect, url_for, current_app, abort
from ..evento.models import Evento
from forms import InscricaoForm
from models import Encontrista, CasalEncontrista
import time
from extensions import db

encontrista = Blueprint('encontrista', __name__)

@encontrista.route('/inscricao/<int:id>/', methods=['GET', 'POST'])
def inscricao(id):
    evento = Evento.query.filter(Evento.aberto_inscricao == True, Evento.dt_evento >= time.strftime("%d/%m/%Y"), Evento.id == id).first()
    
    if not evento:
        flash(u'Evento inválido ou inscrições encerradas!', "warning")

    form = InscricaoForm()
    
    if request.method == "POST" and form.validate_on_submit():
        #try:
        #adiciona esposa
        inscricao_esposa = Encontrista()
        
        inscricao_esposa.nome = form.nome[0].data
        
        if form.dt_nascimento[0].data <> '':
            inscricao_esposa.dt_nascimento = form.dt_nascimento[0].data
        
        inscricao_esposa.email = form.email[0].data
        inscricao_esposa.celular = form.celular[0].data
        inscricao_esposa.sexo = 'F'

        #adiciona esposo        
        inscricao_esposo = Encontrista()
        
        inscricao_esposo.nome = form.nome[1].data

        if form.dt_nascimento[1].data <> '':
            inscricao_esposo.dt_nascimento = form.dt_nascimento[1].data

        inscricao_esposo.email = form.email[1].data
        inscricao_esposo.celular = form.celular[1].data
        inscricao_esposo.sexo = 'M'
        
        db.session.add(inscricao_esposa)
        db.session.add(inscricao_esposo)
        db.session.flush()

        #insere casal
        ce = CasalEncontrista()
        
        if form.rua.data <> '':
            ce.rua = form.rua.data
            
        if form.cep.data <> '':
            ce.cep = form.cep.data
        
        if form.numero.data <> '':
            ce.numero = form.numero.data
        
        if form.complemento.data <> '':
            ce.complemento = form.complemento.data
        
        if form.cidade.data <> '':
            ce.cidade = form.cidade.data
        
        if form.bairro.data <> '':
            ce.bairro = form.bairro.data
        
        if form.uf.data <> '':
            ce.uf = form.uf.data
        
        if form.telefone_residencial.data <> '':
            ce.telefone_residencial = form.telefone_residencial.data

        ce.dt_casamento = form.dt_casamento.data
        ce.paroquia_casamento = form.dt_casamento.data
        ce.id_esposa = inscricao_esposa.id
        ce.id_esposo = inscricao_esposo.id
        ce.id_encontro = id

        db.session.add(ce)
        
        db.session.commit()
        flash(u"Inscrição realizada com sucesso!", "success")
        #except Exception:
        #    db.session.rollback()
        #    flash(u"Erro ao realizar a inscrição!", "success")

        return redirect("/encontrista/inscricao/" + str(id))

    return render_template("encontrista/inscricao.html", form = form, menu='eventos', evento=evento)