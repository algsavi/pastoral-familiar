#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect
from models import Nucleo
from forms import NucleoForm
from extensions import db
from sqlalchemy.exc import IntegrityError

nucleo = Blueprint('nucleo', __name__)

@nucleo.route('/')
def index():
    nucleos = Nucleo.query.order_by(Nucleo.descricao)

    return render_template('nucleo/listar.html', menu='cadastros', nucleos=nucleos)

@nucleo.route('/novo', methods=['GET', 'POST'])
def novo():
    form = NucleoForm()

    if request.method == "POST" and form.validate_on_submit():
        nucleo = Nucleo()
        form.populate_obj(nucleo)

        db.session.add(nucleo)
        db.session.commit()

        flash("Núclo adicionado com sucesso!")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros", submenu='encontro')

@nucleo.route('/<int:id>', methods=['GET', 'POST'])
def editar(id):
    nucleo = Nucleo.query.get_or_404(id)
    form = NucleoForm(obj=nucleo)

    if request.method == "POST" and form.validate_on_submit():
        nucleo = Nucleo()
        form.populate_obj(nucleo)

        db.session.add(nucleo)
        db.session.commit()

        flash("Núcleo editado com sucesso!")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros", submenu='encontro')

@nucleo.route('/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
    if id <> None and request.method == "GET":
        nucleo = Nucleo.query.get_or_404(id)

        try:
            db.session.delete(nucleo)
            db.session.commit()
        except IntegrityError:
            flash(u'ERRO: Existem agentes vinculados ao Núcleo!')

    return redirect("/nucleo/")