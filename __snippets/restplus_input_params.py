from flask import Flask, request
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
todos = {'t1': 'sell all belongings'}

parser = reqparse.RequestParser()
parser.add_argument('todo_id', type=str)

@api.route('/todo')
class TodoSimple(Resource):
	@api.doc(params={'todo_id': {'description': 'ID of todo'}})
	def get(self):
		todo_id = parser.parse_args()['todo_id']
		return {todo_id: todos[todo_id]}

app.run(debug=True)

"""
http GET "http://localhost:5000/todo?todo_id=t1"

http://flask-restplus.readthedocs.io/en/stable/parsing.html
"""
