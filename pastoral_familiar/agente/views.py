#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Blueprint, session, render_template, request, flash, redirect, url_for, current_app, abort
from extensions import db, AnonymousIdentity, login_required, current_user, or_, and_
from models import Agente
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from forms import AgenteFormInserir, AgenteFormEditar
from ..nucleo.models import Nucleo
from collections import namedtuple
from functools import partial
from config import DATA_PER_PAGE
from flask.ext.principal import Permission, UserNeed, RoleNeed, identity_loaded
from flask.ext.security.utils import encrypt_password
from collections import namedtuple
from functools import partial
from pastoral_familiar.utils import is_accessible


EditarNucleoNeed = namedtuple(u'coordenador_nucleo', ['method', 'value'])
EditarAgenteNucleoNeed = partial(EditarNucleoNeed, 'editar')


class EditarAgenteNucleoPermission(Permission):
    def __init__(self, id_nucleo):
        need = EditarAgenteNucleoNeed(unicode(id_nucleo))
        super(EditarAgenteNucleoPermission, self).__init__(need)
        

agente = Blueprint('agente', __name__)
coordenador_pastoral = Permission(RoleNeed('coordenador_pastoral'))
coordenador_nucleo = Permission(RoleNeed('coordenador_nucleo'))


#Controle de permissões
def _on_principal_init(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))

    identity.provides.add(EditarAgenteNucleoNeed(unicode(current_user.id_nucleo)))


identity_loaded.connect(_on_principal_init)


@agente.route('/')
@agente.route('/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
    agentes = Agente.query.join(Nucleo, Agente.id_nucleo==Nucleo.id).add_columns(Agente.id, Agente.nome,
                    Nucleo.descricao, Agente.coordenador_nucleo, Agente.coordenador_pastoral, Agente.email,
                    Agente.celular, Nucleo.id.label("id_nucleo")).filter(or_(Nucleo.id==g.user.id_nucleo,
                    g.user.coordenador_pastoral==True, g.user.coordenador_nucleo==True),
                    and_(Agente.active==True)).order_by(Nucleo.descricao, Agente.nome).paginate(page, DATA_PER_PAGE, False)

    return render_template('agente/listar.html', menu='agente', cur_page=page, agentes=agentes)


@agente.route('/novo/', methods=['GET', 'POST'])
def novo():
    nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]
    form = AgenteFormInserir()
    form.id_nucleo.choices = nucleos
    form.id_nucleo.choices.insert(0, (0, "Selecione..."))

    if request.method == "POST" and form.validate_on_submit():
        agente = Agente()
        form.populate_obj(agente)
        
        agente.active = True
        agente.coordenador_nucleo = False
        agente.coordenador_pastoral = False
        agente.password = encrypt_password(agente.password)

        try:
            db.session.add(agente)
            db.session.commit()
            
            flash("Agente adicionado com sucesso!", "success")
            
            return redirect("/agente/")
        except Exception:
            db.session.rollback()
            flash(u'ERRO: E-mail já utilizado!', "warning")

    return render_template("agente/form.html", form = form, menu='agente')


@agente.route('/editar/<int:id>/', methods=['GET', 'POST'])
@login_required
def editar(id):
    agente = Agente.query.get_or_404(id)
    permission = EditarAgenteNucleoPermission(agente.id_nucleo)
    
    if is_accessible() or g.user.id == id or (is_accessible(roles_accepted=('coordenador_nucleo', )) and permission.can()):
        nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]
        
        form = AgenteFormEditar(obj=agente)

        form.id_nucleo.choices = nucleos
        form.id_nucleo.choices.insert(0, (0, "Selecione...")) 
        
        if request.method == "POST" and form.validate_on_submit():
            coordenador_nucleo = agente.coordenador_nucleo
            form.populate_obj(agente)
            
            if g.user.coordenador_pastoral == False:
                agente.coordenador_nucleo = coordenador_nucleo

            db.session.commit()

            flash(u"Agente editado com sucesso!", "success")
            return redirect("/agente/")
    else:
        abort(403)       

    return render_template("agente/form_editar.html", form = form, menu='agente')


@agente.route('/excluir/<int:id>/', methods=['GET', 'POST'])
@login_required
def excluir(id):
    permission = EditarAgenteNucleoPermission(g.user.id_nucleo)

    if is_accessible() or g.user.id == id or (is_accessible(roles_accepted=('coordenador_nucleo', )) and permission.can()):
        if id <> None and request.method == "GET":
            agente = Agente.query.get_or_404(id)

            agente.active = False

            db.session.commit()
            
            flash(u"Agente excluído com sucesso!", "success")
    else:
        abort(403)  

    return redirect("/agente/")