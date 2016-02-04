#! /usr/bin/env python
# -*- coding: utf-8 -*-

def get_current_user():
    from flask.ext.security import current_user
    return current_user
  

def is_accessible(roles_accepted=None, user=None):
    user = user or get_current_user()
    if user.has_role('coordenador_pastoral'):
        return True
    if roles_accepted:
        accessible = any(user.has_role(role) for role in roles_accepted)
        return accessible
    return False