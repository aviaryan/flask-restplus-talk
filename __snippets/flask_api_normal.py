from flask import Flask, request, jsonify

app = Flask(__name__)
todos = {}

@app.route('/todos/<string:todo_id>', methods=['GET', 'POST'])
def todoList(todo_id):
	if request.method == 'POST':
		todos[todo_id] = request.form['data']
		return jsonify({todo_id: request.form['data']})
	else:
		return jsonify({todo_id: todos[todo_id]})

app.run(debug=True)

"""
http GET http://localhost:5000/todos/t1
http -f POST http://localhost:5000/todos/t1 data='give talk'
"""
