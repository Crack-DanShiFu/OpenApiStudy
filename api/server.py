import datetime
import json
import locale

from flask import jsonify

from exts import db
from model.model import *


def query_city_list():
    query = db.session().query(CityName).all()
    return json.dumps([i.to_json() for i in query], ensure_ascii=False)


def query_month_data_by_city(city):
    query = db.session().query(MonthData).filter_by(cityName=city).all()
    return json.dumps([i.to_json() for i in query], ensure_ascii=False)


# query_day_data_by_city

def query_day_data_by_city(city, month):
    query = db.session().query(DayData).filter(DayData.time_point.ilike(month + '%')).filter_by(cityName=city).all()
    return json.dumps([i.to_json() for i in query], ensure_ascii=False)


# query_all_day_data
def query_all_day_data(city):
    query = db.session().query(DayData).filter_by(cityName=city).all()
    return json.dumps([i.to_json() for i in query], ensure_ascii=False)


def query_lately_aqi_city():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    now_y, now_m, now_d = yesterday.strftime('%Y-%m-%d').split('-')
    s = now_y + '-' + now_m + '-' + now_d
    query = db.session().query(DayData, CityName).filter(DayData.time_point == s).filter(
        DayData.cityName == CityName.city).all()
    result = {}
    for q in query:
        result[q[1].regionid] = [q[0].cityName, q[0].aqi]
    return json.dumps(result, ensure_ascii=False)
