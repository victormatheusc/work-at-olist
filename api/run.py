from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class CallRecord(Resource):

    def get(self):
        return {'success': 'GET method is working!'}, 200

    def post(self):
        return {'success': 'POST method is working!'}, 200


api.add_resource(CallRecord, '/')

if __name__ == '__main__':
    app.run(debug=True)
