# -*- coding: utf-8 -*-

import json

from app import app, login_manager
from flask import request, jsonify, render_template
from modules import common, models
from flask_login import login_user, \
        logout_user, login_required, \
        current_user


@login_manager.user_loader
def load_user(id):
    return models.User.get_user(id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    info     = json.loads(request.data)
    email    = info.get('email')
    password = info.get('password')
    user     = models.User.object(email = email, password = password)

    if user:
        login_user(user)
    else:
        pass


@app.route('/')
# @login_required
def index():
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    pass
