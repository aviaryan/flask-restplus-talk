from flask import Flask, request
from flask_restplus import Resource, Api
from errors import NotFoundError

app = Flask(__name__)
api = Api(app)
todos = {'t1': 'do something'}

@api.errorhandler(NotFoundError)
def handle_error(error):
    return error.to_dict(), getattr(error, 'code')

@api.route('/todos/<string:todo_id>')
class TodoSimple(Resource):
	def get(self, todo_id):
		if todo_id not in todos:
			raise NotFoundError()
		return {todo_id: todos[todo_id]}

app.run(debug=True)

"""
http GET http://localhost:5000/todos/t1
"""
