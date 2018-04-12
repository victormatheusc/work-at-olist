from flask_restful import Resource
from flask import request


class CallRecord(Resource):

    def get(self, phonenumber=None, month=None, year=None):
        if phonenumber:
            return {'success': 'GET method is working!'}, 200
        return {'error': 'Phone number is required!'}, 502

    def post(self, phonenumber=None, month=None, year=None):
        if phonenumber or month or year:
            return {"error": "no route is required"}, 502
        call_data = request.get_json()
        if call_data:
            return call_data, 200
        return {'success': 'POST method is working!'}, 200
