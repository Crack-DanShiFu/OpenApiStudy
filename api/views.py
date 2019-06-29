import json
import os

from flask import request, app, send_from_directory, abort

from api.server import *
from . import api


@api.route('/')
def index():
    return "api"


# @api.route('/get_city_list/')
# def get_city_list():
#     return query_city_list()


# query_month_data
@api.route('/get_month_data/')
def get_month_data_by_city():
    city = request.args.get('city')
    return query_month_data_by_city(city)


# get_day_data
@api.route('/get_day_data/')
def get_day_data_by_city():
    city = request.args.get('city')
    month = request.args.get('month')
    return query_day_data_by_city(city, month)


# get_all_day_data
@api.route('/get_all_day_data/')
def get_all_day_data():
    city = request.args.get('city')
    return query_all_day_data(city)


# query_lately_data
@api.route('/get_lately_aqi/')
def get_lately_data_city():
    provinces_id = request.args.get('provinces')
    return query_lately_aqi_city(provinces_id)


# get_provinces_aqi
@api.route('/get_provinces_aqi/')
def get_provinces_aqi():
    provinces_id = request.args.get('provinces') + '0000'
    filename = 'static/temp/' + provinces_id + '.xls'
    if os.path.exists(filename):
        directory = os.getcwd()  # 假设在当前目录s
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        abort(404)


# year_data
@api.route('/year_data/')
def get_year_data():
    year = request.args.get('year')
    filename = 'static/temp/' + year + '.xlsx'
    if os.path.exists(filename):
        directory = os.getcwd()  # 假设在当前目录s
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        abort(500)


@api.route('/downloads_day_data/')
def get_day_data():
    day = request.args.get('day')
    return query_day_data(day)


@api.route('/update_day_excel')
def update_day_excel():
    query_update_day_excel()
    return "success"
