from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import BLOB, INTEGER
from argon2 import PasswordHasher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import datetime
import uuid
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///totally_not_my_privateKeys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ph = PasswordHasher()

# Assuming the AES key is correctly set in your environment variable
aes_key = os.environ.get('NOT_MY_KEY')
if aes_key is None:
    raise ValueError("The AES key has not been provided in the environment variables.")

# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_login = db.Column(db.DateTime)

class AuthLog(db.Model):
    __tablename__ = 'auth_logs'
    id = db.Column(db.Integer, primary_key=True)
    request_ip = db.Column(db.String(15), nullable=False)
    request_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Key(db.Model):
    __tablename__ = 'keys'
    id = db.Column(db.Integer, primary_key=True)  # Renamed from 'kid' to 'id' to match the Go code expectation
    encrypted_key = db.Column(BLOB, nullable=False)
    exp = db.Column(INTEGER, nullable=False)

# Helper functions for AES Encryption
def encrypt_data(data, key):
    try:
        # Decode the base64 encoded key
        key = base64.b64decode(key)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(data.encode()) + encryptor.finalize()
        return encrypted
    except Exception as e:
        app.logger.error(f"Encryption failed: {e}")
        return None


@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    password = str(uuid.uuid4())
    hashed_password = ph.hash(password)

    user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'password': password}), 201

@app.route('/auth', methods=['POST'])
def authenticate():
    user_id = request.json.get('user_id')
    
    # Perform your actual user authentication logic here
    # For demonstration, we assume authentication is always successful
    if user_id:
        auth_log = AuthLog(request_ip=request.remote_addr, user_id=user_id)
        db.session.add(auth_log)
        db.session.commit()
        return jsonify({'status': 'success'}), 200

    # If authentication fails or 'user_id' is not provided
    return jsonify({'error': 'Authentication failed'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Be cautious: this will delete all existing data
        db.create_all()  # Recreate tables with the correct schema
    app.run(debug=True, port=8080)
