from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env (if available)
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Products data
products = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    # Get port from environment or default to 3030
    port = int(os.getenv("PORT", 3030))
    app.run(host="0.0.0.0", port=port)
