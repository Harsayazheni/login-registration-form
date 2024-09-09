from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Temporary storage for users
users = {}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = generate_password_hash(data.get('password'), method='sha256')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    users[username] = {'email': email, 'password': password}
    return jsonify({'message': 'Registration successful'}), 200

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

@app.route('/static/css/styles.css')
def serve_static(styles):
    return send_from_directory(os.path.join(app.root_path, 'static'), styles)

if __name__ == '__main__':
    app.run(debug=True)
