from flask import Flask
from exts import db
import config

from model.model import *

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object(config)
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# api
from api import api

app.register_blueprint(api, url_prefix='/api')
# pageManage
from pageManage import pageManage

app.register_blueprint(pageManage, url_prefix='/')

# manage
from manage import manage

app.register_blueprint(manage, url_prefix='/manage')

if __name__ == '__main__':
    app.run()
