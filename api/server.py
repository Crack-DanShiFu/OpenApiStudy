import json
import locale

from flask import jsonify

from exts import db
from model.model import *


def query_month_data():
    query = db.session().query(MonthData, CityName).filter(MonthData.cityName == CityName.city).all()
    result = []
    for q in query:
        re = [].append(1)
        result.append(re)
    print(result[:20])
    # sorted(result, cmp=locale.strcoll, key=lambda x: x['cityName'])
    return ''


def query_city_list():
    query = db.session().query(CityName).all()
    return json.dumps([i.to_json() for i in query], ensure_ascii=False)


def query_month_data_by_city(city):
    query = db.session().query(MonthData).filter_by(cityName=city).all()
    return json.dumps([i.to_json() for i in query[::-1]])
