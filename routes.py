from flask import Blueprint, request, jsonify
import db

routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/")
def index():
    return "Python's server is on"

@routes_bp.route('/api/addtodo', methods=['POST'])
def add_todos():
    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return {"error": "Missing data"}, 400

    conn = db.get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO todos (title, description) VALUES (%s, %s);", (title, description))
        conn.commit()
        return {"message": "Todo added successfully"}, 201
    except Exception as e:
        conn.rollback()
        return {"error": "An error occurred", "details": str(e)}, 500
    finally:
        cur.close()
        conn.close()

@routes_bp.route('/api/todos', methods=['GET'])
def get_todos():
    conn = db.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos;")
    todos = cur.fetchall()
    cur.close()
    conn.close()

    todos_list = []
    for todo in todos:
        todo_dict = {
            "id": todo[0],
            "title": todo[1],
            "description": todo[2]
        }
        todos_list.append(todo_dict)

    return jsonify({"todos": todos_list})

# delete task
@routes_bp.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todos(id):
    print(id)
    conn = db.get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Todo deleted successfully"}), 200