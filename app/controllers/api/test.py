from sanic_restful import Resource
from app.helpers.rest import *
import os


class AboutNow(Resource):
    async def get(self, request, id):
        return response(200, message=id)
