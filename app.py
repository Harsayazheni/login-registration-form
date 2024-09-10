from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('home.html')

# Registration page (GET)
@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

# Registration handling (POST)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))

    users = {}  # In a real app, this should come from a database
    users[username] = {'email': email, 'password': password}
    
    return jsonify({'message': 'Registration successful'}), 200

# Login page (GET)
@app.route('/home', methods=['GET'])
def login_page():
    return render_template('home.html')

# Login handling (POST)
@app.route('/home', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = {}  # In a real app, this should come from a database
    user = users.get(username)
    
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

# Serving static files (e.g., CSS)
@app.route('/static/css/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/css'), filename)

if __name__ == '__main__':
    app.run(debug=True)
