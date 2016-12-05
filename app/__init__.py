# -*- coding: utf-8 -*-

'''
    Author: xdlove
'''

from flask import Flask

app = Flask(__name__)

from app.core import views
