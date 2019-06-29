import json

from sqlalchemy import func

from exts import db
from model.model import *


def query_count_fo_all():
    daydata = DayData.query.count()
    monthdata = MonthData.query.count()
    least_time = db.session.query(func.max(DayData.time_point)).scalar()

    provinces_list = db.session().query(Provinces).all()
    year_list = [str(i + 2013) for i in range(7)]

    return {'year_list': year_list, 'daydata': daydata, 'monthdata': monthdata, 'least_time': least_time,
            'provinces_list': provinces_list}
