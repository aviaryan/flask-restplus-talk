from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
todos = {}

@api.route('/todos/<string:todo_id>')
class TodoSimple(Resource):
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	def post(self, todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}

app.run(debug=True)

"""
http GET http://localhost:5000/todos/t1
http -f POST http://localhost:5000/todos/t1 data='give talk'
"""
