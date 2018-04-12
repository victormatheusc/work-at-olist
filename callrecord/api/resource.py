from flask_restful import Resource


class CallRecord(Resource):

    def get(self):
        return {'success': 'GET method is working!'}, 200

    def post(self):
        return {'success': 'POST method is working!'}, 200