from sanic import Blueprint
from sanic_restful import Api
from .test import *


api_blueprint = Blueprint(__name__, url_prefix='/api')
api = Api(api_blueprint)
api.add_resource(AboutNow, '/test/<id>')

