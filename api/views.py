import json

from api.server import *
from . import api


@api.route('/')
def index():
    return "api"


@api.route('/get_month_data/')
def get_month_data():
    return query_month_data()
