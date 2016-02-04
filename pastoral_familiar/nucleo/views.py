#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect, g
from models import Nucleo
from forms import NucleoForm
from extensions import db, current_user, login_required
from sqlalchemy.exc import IntegrityError
from ..agente.views import coordenador_pastoral
from config import DATA_PER_PAGE

nucleo = Blueprint('nucleo', __name__)
    

@nucleo.route('/')
@nucleo.route('/<int:page>', methods = ['GET', 'POST'])
@coordenador_pastoral.require(http_exception=403)
def index(page = 1):
    nucleos = Nucleo.query.order_by(Nucleo.descricao).paginate(page, DATA_PER_PAGE, False)

    return render_template('nucleo/listar.html', menu='cadastros', cur_page=page, nucleos=nucleos)


@nucleo.route('/novo/', methods=['GET', 'POST'])
@coordenador_pastoral.require(http_exception=403)
def novo():
    form = NucleoForm()

    if request.method == "POST" and form.validate_on_submit():
        nucleo = Nucleo()
        form.populate_obj(nucleo)

        db.session.add(nucleo)
        db.session.commit()

        flash(u"Núcleo adicionado com sucesso!", "success")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros")


@nucleo.route('/editar/<int:id>/', methods=['GET', 'POST'])
@coordenador_pastoral.require(http_exception=403)
def editar(id):
    nucleo = Nucleo.query.get_or_404(id)
    form = NucleoForm(obj=nucleo)

    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(nucleo)

        db.session.commit()

        flash(u"Núcleo editado com sucesso!", "success")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros")


@nucleo.route('/excluir/<int:id>/', methods=['GET', 'POST'])
@login_required
@coordenador_pastoral.require(http_exception=403)
def excluir(id):
    if id <> None and request.method == "GET":
        nucleo = Nucleo.query.get_or_404(id)

        try:
            db.session.delete(nucleo)
            db.session.commit()
            
            flash(u'Núcleo excluído com sucesso!', "success")
        except IntegrityError:
            flash(u'ERRO: Existem agentes vinculados ao Núcleo!', "warning")

    return redirect("/nucleo/")