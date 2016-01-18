#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Blueprint, render_template, request, flash, redirect
from extensions import db
from models import Agente 
from forms import AgenteForm
from ..nucleo.models import Nucleo

agente = Blueprint('agente', __name__)

@agente.route('/')
def index():
    agentes = Agente.query.join(Nucleo, Agente.id_nucleo==Nucleo.id).add_columns(Agente.nome, Nucleo.descricao).order_by(Agente.nome)

    return render_template('agente/listar.html', menu='agente', agentes=agentes)


@agente.route('/novo', methods=['GET', 'POST'])
def novo():
    nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]
    form = AgenteForm()
    form.id_nucleo.choices = nucleos
    form.id_nucleo.choices.insert(0, (0, "Selecione..."))

    if request.method == "POST" and form.validate_on_submit():
        agente = Agente()
        form.populate_obj(agente)
        
        agente.senha = agente.define_senha(agente.senha)

        db.session.add(agente)
        db.session.commit()

        flash("Agente adicionado com sucesso!")
        return redirect("/agente/")

    return render_template("agente/form.html", form = form, menu='agente')

