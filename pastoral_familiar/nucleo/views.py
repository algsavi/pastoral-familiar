#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, flash, redirect, g
from models import Nucleo
from forms import NucleoForm
from extensions import db, login_required, current_user
from sqlalchemy.exc import IntegrityError
from ..agente.views import admin_permission

nucleo = Blueprint('nucleo', __name__)

@nucleo.before_request
def before_request():
    g.user = current_user


@nucleo.route('/')
@admin_permission.require(http_exception=403)
def index():
    nucleos = Nucleo.query.order_by(Nucleo.descricao)

    return render_template('nucleo/listar.html', menu='cadastros', nucleos=nucleos)


@nucleo.route('/novo/', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def novo():
    form = NucleoForm()

    if request.method == "POST" and form.validate_on_submit():
        nucleo = Nucleo()
        form.populate_obj(nucleo)

        db.session.add(nucleo)
        db.session.commit()

        flash(u"Nucleo adicionado com sucesso!")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros", submenu='encontro')


@nucleo.route('/editar/<int:id>/', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def editar(id):
    nucleo = Nucleo.query.get_or_404(id)
    form = NucleoForm(obj=nucleo)

    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(nucleo)

        db.session.commit()

        flash(u"Nucleo editado com sucesso!")
        return redirect("/nucleo/")

    return render_template("nucleo/form.html", form = form, menu="cadastros", submenu='encontro')

@nucleo.route('/excluir/<int:id>/', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def excluir(id):
    if id <> None and request.method == "GET":
        nucleo = Nucleo.query.get_or_404(id)

        try:
            db.session.delete(nucleo)
            db.session.commit()
        except IntegrityError:
            flash(u'ERRO: Existem agentes vinculados ao Nucleo!')

    return redirect("/nucleo/")