from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from db import db
from routes import register_routes

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
register_routes(app)

@app.route("/")
def home():
    return {"message": "Hello from Flask"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
