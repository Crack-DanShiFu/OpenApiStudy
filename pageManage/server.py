import json

from exts import db
from model.model import *


def query_city_list():
    query = db.session().query(CityName).all()
    result = {}
    for i in query:
        if not (i.first_letter in result.keys()):
            result[i.first_letter] = []
        result[i.first_letter].append(i.to_json())
    return result


def query_provinces_list():
    query = db.session().query(Provinces).all()
    return [i.to_json() for i in query]


def query_month_data(city):
    query = db.session().query(MonthData).filter_by(cityName=city).all()
    return {'city': city, 'result': [i.to_json() for i in query]}


def query_day_data(city, month):
    query = db.session().query(DayData).filter(DayData.time_point.ilike(month + '%')).filter_by(
        cityName=city).all()
    return {'city': city, 'month': month, 'result': [i.to_json() for i in query]}


def query_provinces_data(provinces):
    query = db.session().query(CityName).filter(CityName.regionid.ilike(provinces + '%'))
    return {'provinces': provinces, 'result': [i.to_json() for i in query]}
