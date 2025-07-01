from flask import request, jsonify
from models import User
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered"}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"message": "Login successful", "email": user.email}), 200

    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify([user.serialize() for user in User.query.all()])
