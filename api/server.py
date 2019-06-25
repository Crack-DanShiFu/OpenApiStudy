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
