# -*- coding: utf-8 -*-

'''
    Author: xdlove
'''

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'core.views.login'

from app.core import views
