todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

def todo_list():
    json_text = jsonify(todos)
    return json_text

def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'