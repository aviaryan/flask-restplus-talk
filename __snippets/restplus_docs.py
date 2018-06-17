from flask import Flask, request
from flask_restplus import fields, Api, Resource

app = Flask(__name__)
api = Api(app)
todos = {'t1': {'task': 'task 1', 'priority': 2}}

TASK_MODEL = api.model('Task', {
	'task': fields.String,
	'priority': fields.Integer
})

@api.route('/todos/<string:todo_id>')
class TodoWithModel(Resource):
	@api.doc('get_todo', params={'indent': {'description': 'how many indents to the response'}})
	@api.header('Authorization', 'Bearer {token}')
	@api.marshal_with(TASK_MODEL)
	def get(self, todo_id):
		"""gets a particular todo"""
		return todos[todo_id]

app.run(debug=True)

"""
curl -X GET --header 'Accept: application/json' \
	--header 'Authorization: secret_token' 'http://localhost:5000/todos/t1?indent=4'
"""

