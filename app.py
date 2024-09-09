from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Temporary storage for users
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = generate_password_hash(data['password'], method='sha256')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    users[username] = {'email': email, 'password': password}
    return jsonify({'message': 'Registration successful'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

if __name__ == '__main__':
    app.run(debug=True)
