#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Blueprint, render_template, request, flash, redirect, url_for, current_app, abort
from extensions import db, lm, login_required, current_user, login_user, logout_user, Permission, RoleNeed, identity_loaded, identity_changed, Identity, UserNeed, or_, and_
from models import Agente
from sqlalchemy.exc import InvalidRequestError, IntegrityError
from forms import AgenteFormInserir, AgenteFormEditar, LoginForm
from ..nucleo.models import Nucleo
from collections import namedtuple
from functools import partial

agente = Blueprint('agente', __name__)
admin_permission = Permission(RoleNeed('admin'))

#Controle de permissões
def _on_principal_init(sender, identity):
    if identity.id == 'admin':
        identity.provides.add(RoleNeed('admin'))

identity_loaded.connect(_on_principal_init)

@agente.before_request
def before_request():
    g.user = current_user


@agente.route('/')
@login_required
def index():
    agentes = Agente.query.join(Nucleo, Agente.id_nucleo==Nucleo.id).add_columns(Agente.id, Agente.nome, Nucleo.descricao).filter(or_(Nucleo.id==g.user.id_nucleo, g.user.coordenador_pastoral==True), and_(Agente.ativo==True)).order_by(Agente.nome)

    return render_template('agente/listar.html', menu='agente', agentes=agentes)


@agente.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        agente = Agente.query.filter(Agente.email==form.email.data).first()

        if agente is not None:
            if agente.verifica_senha(form.senha.data):
                login_user(agente, form.remember_me.data)
                
                if agente.coordenador_pastoral == True:
                    identity_changed.send(current_app._get_current_object(), identity=Identity('admin'))
                else:
                    identity_changed.send(current_app._get_current_object(), identity=Identity('agente'))

                return redirect(url_for("agente.index"))
            else:
                flash(u"Usuário/senha inválidos!")

    return render_template('agente/login.html', form = form)


@agente.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('agente.login'))


@lm.user_loader
def load_user(email):
    return Agente.query.filter(Agente.email==email).first()


@agente.route('/novo', methods=['GET', 'POST'])
def novo():
    nucleos = [(c.id, c.descricao) for c in Nucleo.query.order_by(Nucleo.descricao).all()]
    form = AgenteFormInserir()
    form.id_nucleo.choices = nucleos
    form.id_nucleo.choices.insert(0, (0, "Selecione..."))

    if request.method == "POST" and form.validate_on_submit():
        agente = Agente()
        form.populate_obj(agente)
        
        agente.ativo = True
        agente.coordenador_nucleo = False
        agente.coordenador_pastoral = False
        agente.define_senha(agente.senha)

        try:
            db.session.add(agente)
            db.session.commit()
            
            flash("Agente adicionado com sucesso!")
            
            return redirect("/agente/")
        except Exception:
            db.session.rollback()
            flash(u'ERRO: E-mail já utilizado!')        

    return render_template("agente/form.html", form = form, menu='agente')

@login_required
@agente.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    agente = Agente.query.get_or_404(id)

    if g.user.id <> id and g.user.coordenador_pastoral==False:
        if g.user.coordenador_nucleo == False or (g.user.coordenador_nucleo == True and g.user.id_nucleo <> agente.id_nucleo):
            abort(404)
    
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

        flash(u"Agente editado com sucesso!")
        return redirect("/agente/")

    return render_template("agente/form_editar.html", form = form, menu="cadastros", submenu='encontro')


@agente.route('/excluir/<int:id>', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def excluir(id):
    if id <> None and request.method == "GET":
        agente = Agente.query.get_or_404(id)

        agente.ativo = False

        db.session.commit()

    return redirect("/agente/")
