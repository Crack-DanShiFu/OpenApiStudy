import json

from api.server import *
from . import api


@api.route('/')
def index():
    return "api"
