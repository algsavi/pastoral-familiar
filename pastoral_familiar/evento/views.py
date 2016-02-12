#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Blueprint, render_template, request, flash, redirect, url_for, current_app, abort
from extensions import db, login_required, current_user, login_user, logout_user, Permission, RoleNeed, identity_loaded, identity_changed, Identity, UserNeed, or_, and_
from models import Evento
from ..nucleo.models import Nucleo
from forms import EventoForm
from ..agente.views import coordenador_pastoral, coordenador_nucleo
from config import DATA_PER_PAGE
from pastoral_familiar.utils import is_accessible

evento = Blueprint('evento', __name__)

@evento.route('/')
@evento.route('/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
    eventos = Evento.query.outerjoin(Nucleo, Evento.id_nucleo==Nucleo.id).add_columns(Evento.tx_inscricao, Nucleo.descricao.label("nucleo_descricao"), Evento.id, Evento.descricao, Evento.dt_evento, Evento.id_nucleo).order_by(Evento.dt_evento, Nucleo.id).paginate(page, DATA_PER_PAGE, False)
    print eventos

    return render_template('evento/listar.html', menu='eventos', cur_page=page, eventos = eventos)


@evento.route('/novo/', methods=['GET', 'POST'])
@coordenador_pastoral.require(http_exception=403)
def novo():
    nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]
    
    form = EventoForm()
    form.id_nucleo.choices = nucleos
    form.id_nucleo.choices.insert(0, (0, 'Selecione...'))

    if request.method == "POST" and form.validate_on_submit():
        evento = Evento()
        form.populate_obj(evento)

        if evento.id_nucleo == 0:
            evento.id_nucleo = None

        db.session.add(evento)
        db.session.commit()
        
        flash("Evento adicionado com sucesso!", "success")
        return redirect("/evento/")

        
    return render_template("evento/form.html", form = form, menu='eventos')


@evento.route('/editar/<int:id>/', methods=['GET', 'POST'])
def editar(id):
    evento = Evento.query.get_or_404(id)   
    nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]

    if is_accessible() or (g.user.id_nucleo == evento.id_nucleo):
        form = EventoForm(obj=evento)

        form.id_nucleo.choices = nucleos
        form.id_nucleo.choices.insert(0, (0, "Selecione...")) 
        
        if request.method == "POST" and form.validate_on_submit():
            form.populate_obj(evento)
            
            if evento.id_nucleo == 0:
                evento.id_nucleo = None
            
            db.session.commit()

            flash(u"Evento editado com sucesso!", "success")
            return redirect("/evento/")
    else:
        abort(403)

    return render_template("evento/form.html", form = form, menu='eventos')

@evento.route('/excluir/<int:id>/', methods=['GET', 'POST'])
@coordenador_pastoral.require(http_exception=403)
def excluir(id):
    if id <> None and request.method == "GET":
        evento = Evento.query.get_or_404(id)

        try:
            db.session.delete(evento)
            db.session.commit()
            
            flash(u'Evento excluído com sucesso!', "success")
        except IntegrityError:
            flash(u'ERRO: Existem encontristas vinculados ao Evento!', "warning")

    return redirect("/evento/")