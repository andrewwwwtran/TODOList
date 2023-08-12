from website import create_app
from flask import Flask, jsonify, request, render_template

app = create_app()

tasks = []

# API endpoints to handle CRUD 
@app.route('/api/todolist', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/todolist', methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = {
        'id' : len(tasks) + 1,
        'text' : data['text'],
        'completed' : False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# add API routes for updating and deleting 

@app.route('/')
def index():
    return render_template('template.html', tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True)