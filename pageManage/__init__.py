from flask import Blueprint

pageManage = Blueprint('pageManage', __name__)

from . import views
