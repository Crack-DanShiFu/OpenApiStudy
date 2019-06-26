import json

from api.server import *
from . import api


@api.route('/')
def index():
    return "api"


@api.route('/get_month_data/')
def get_month_data():
    return query_month_data()


@api.route('/get_city_list/')
def get_city_list():
    return query_city_list()


# query_month_data
@api.route('/get_month_data/<city>')
def get_month_data_by_city(city):
    return query_month_data_by_city(city)
