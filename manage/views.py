import json
from flask import render_template, request
from manage.server import *
from . import manage


@manage.route('/')
def index():
    data = query_count_fo_all()
    return render_template('manage.html', data=data)
