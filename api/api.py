from flask import Flask
from flask_restful import Resource, Api

from herucode import HeruCode

app = Flask(__name__)
api = Api(app)


class HeruCodeAPI(Resource):
    def post(self):
        args = self.reqparse.parse_args()
        text = args['text'].strip()
        heru = HeruCode(text)
        return {
            heru.get_total_prepositions(),
            heru.get_total_verbs(),
            heru.get_total_subjunctive_verbs()
        }, 200


api.add_resource(HeruCodeAPI, '/parse', endpoint='heru_code')

if __name__ == '__main__':
    app.run(debug=True)
