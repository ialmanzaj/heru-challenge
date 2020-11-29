from herucode import HeruCode
from flask import Flask, abort, jsonify
from flask_restful import Resource, Api, reqparse
parser = reqparse.RequestParser()


app = Flask(__name__)
api = Api(app)


class HeruCodeAPI(Resource):
    def post(self):
        parser.add_argument('text', type=str)
        args = parser.parse_args()
        text = args['text']

        # add string validation
        heru = HeruCode(text)

        return {
            'prepositions': heru.get_total_prepositions(),
            'verbs': heru.get_total_verbs(),
            'subjunctive_verbs': heru.get_total_subjunctive_verbs(),
            'pretty_numbers': heru.get_pretty_number(),
            'vocabulary_list': heru.get_vocabulary_list(),
        }, 200


api.add_resource(HeruCodeAPI, '/parse')

if __name__ == '__main__':
    app.run(debug=True)
