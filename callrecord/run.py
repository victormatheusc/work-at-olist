from flask import Flask, request
from flask_restful import Api

from api.resource import CallRecord

app = Flask(__name__)
api = Api(app)

api.add_resource(CallRecord, 
    '/',
    '/<int:phonenumber>',
    '/<int:phonenumber>/<int:month>',
    '/<int:phonenumber>/<int:month>/<int:year>'
    )

if __name__ == '__main__':
    app.run(debug=True)
