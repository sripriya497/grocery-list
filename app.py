from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for Webflow

# Load product data from CSV
def load_product_data():
    return pd.read_csv("products.csv")

@app.route('/check_products', methods=['POST'])
def check_products():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415  # Unsupported Media Type
    
    try:
        data = request.get_json()  # Load JSON data
        if not data or "items" not in data:
            return jsonify({"error": "Invalid JSON data"}), 400  # Bad Request
        
        # Example response (Modify this based on your logic)
        return jsonify({"message": "Success", "received_items": data["items"]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
    