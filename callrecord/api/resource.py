from flask_restful import Resource


class CallRecord(Resource):

    def get(self, phonenumber=None, month=None, year=None):
        if phonenumber:
            return {'success': 'GET method is working!'}, 200
        return {'error': 'Phone number is required!'}, 502

    def post(self):
        return {'success': 'POST method is working!'}, 200
