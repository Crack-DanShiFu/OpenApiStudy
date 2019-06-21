import json

from pageManage.server import *
from . import pageManage


@pageManage.route('/')
def index():
    return ""
