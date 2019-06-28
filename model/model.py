import json
import time

from exts import db


class User(db.Model):
    __tableName__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))


class CityName(db.Model):
    __tableName__ = 'city_name'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(10))
    first_letter = db.Column(db.String(2))
    rank = db.Column(db.Integer)
    regionid = db.Column(db.Integer)

    def to_json(self):
        json_data = {
            'city': self.city,
            'first_letter': self.first_letter,
            'rank': self.rank,
            'regionid': self.regionid,
        }
        return json_data


class Provinces(db.Model):
    __tableName__ = 'provinces'
    provinces_name = db.Column(db.String(10), primary_key=True, )
    provinces_id = db.Column(db.String(6))

    def to_json(self):
        json_data = {
            'provinces_name': self.provinces_name,
            'provinces_id': self.provinces_id,
        }
        return json_data


class DayData(db.Model):
    __tableName__ = 'day_data'
    cityName = db.Column(db.String(10), primary_key=True)
    time_point = db.Column(db.Date, primary_key=True)
    aqi = db.Column(db.Integer)
    pm2_5 = db.Column(db.Integer)
    pm10 = db.Column(db.Integer)
    so2 = db.Column(db.Integer)
    no2 = db.Column(db.Integer)
    co = db.Column(db.Float)
    o3 = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    quality = db.Column(db.String(5))

    def to_json(self):
        json_data = {
            'cityName': self.cityName,
            'time_point': str(self.time_point),
            'aqi': self.aqi,
            'pm2_5': self.pm2_5,
            'pm10': self.pm10,
            'so2': self.so2,
            'no2': self.no2,
            'co': self.co,
            'o3': self.o3,
            'rank': self.rank,
            'quality': self.quality,
        }
        return json_data


class MonthData(db.Model):
    __tableName__ = 'month_data'
    cityName = db.Column(db.String(10), primary_key=True)
    time_point = db.Column(db.String(10), primary_key=True)
    aqi = db.Column(db.Integer)
    max_aqi = db.Column(db.Integer)
    min_aqi = db.Column(db.Integer)
    pm2_5 = db.Column(db.Integer)
    pm10 = db.Column(db.Integer)
    so2 = db.Column(db.Integer)
    no2 = db.Column(db.Integer)
    co = db.Column(db.Float)
    o3 = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    quality = db.Column(db.String(5))

    def to_json(self):
        json_data = {
            'cityName': self.cityName,
            'time_point': self.time_point,
            'aqi': self.aqi,
            'max_aqi': self.max_aqi,
            'min_aqi': self.min_aqi,
            'pm2_5': self.pm2_5,
            'pm10': self.pm10,
            'so2': self.so2,
            'no2': self.no2,
            'co': self.co,
            'o3': self.o3,
            'rank': self.rank,
            'quality': self.quality,
        }
        return json_data
