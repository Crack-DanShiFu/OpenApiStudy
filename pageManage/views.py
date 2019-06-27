import json
from flask import render_template, request
from pageManage.server import *
from . import pageManage


@pageManage.route('/')
def index():
    data1 = query_city_list()
    data2 = query_provinces_list()
    return render_template('index.html', data=[data1, data2])


# monthdata
@pageManage.route('/monthdata/')
def month_data():
    city = request.args.get('city')
    data = query_month_data(city)
    return render_template('monthdata.html', data=data)


# daydata
@pageManage.route('/daydata/')
def day_data():
    city = request.args.get('city')
    month = request.args.get('month')
    data = query_day_data(city, month)
    return render_template('daydata.html', data=data)


# provinces_data?provinces=天津市
@pageManage.route('/provinces_data/')
def provinces_data():
    provinces = request.args.get('provinces')
    data = query_provinces_data(provinces)
    return render_template('provinces.html', data=data)
