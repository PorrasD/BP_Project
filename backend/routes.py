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

    @app.route('/users')
    def get_users():
        users = User.query.all()
        return jsonify([user.serialize() for user in users])
