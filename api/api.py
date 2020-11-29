from flask import Flask
from flask_restful import Resource, Api

from herucode import HeruCode

app = Flask(__name__)
api = Api(app)


class HeruCodeAPI(Resource):
    def post(self):
        pass


api.add_resource(HeruCodeAPI, '/parse', endpoint='heru_code')

if __name__ == '__main__':
    app.run(debug=True)
