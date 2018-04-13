from flask_restful import Resource
from flask import request

from .views import save_call_data


class CallRecord(Resource):

    def get(self, phonenumber=None, month=None, year=None):
        if phonenumber:
            return {'success': 'GET method is working'}, 200
        
        return {'error': 'Phone number is required'}, 400

    def post(self, phonenumber=None, month=None, year=None):
        if phonenumber or month or year:
            return {"error": "no route is required"}, 400

        call_data = request.get_json()
        if call_data:
            return save_call_data(call_data)

        return {'error': 'Call information is needed'}, 400
