from flask import Flask, request
from flask_restplus import fields, Api, Resource

app = Flask(__name__)
api = Api(app)
todos = {}

TASK_MODEL = api.model('Task', {
	'task': fields.String,
	'priority': fields.Integer
})

@api.route('/todos/<string:todo_id>')
class TodoWithModel(Resource):
	@api.marshal_with(TASK_MODEL)
	def get(self, todo_id):
		return todos[todo_id]

	@api.expect(TASK_MODEL)
	def put(self, todo_id):
		todos[todo_id] = {'task': self.api.payload['task'], 
			'priority': self.api.payload['priority']}
		return todos[todo_id]

app.run(debug=True)
