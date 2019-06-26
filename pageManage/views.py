import json
from flask import render_template, request
from pageManage.server import *
from . import pageManage


@pageManage.route('/')
def index():
    data = query_city_list()
    return render_template('index.html', data=data)


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
