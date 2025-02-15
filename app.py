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
        data = request.get_json()
    
        if not data or "items" not in data:
            return jsonify({"error": "Invalid request"}), 400
        
        # Ensure 'items' is a list, splitting if necessary
        if isinstance(data["items"], str):
            items = data["items"].split(",")  # Split string into a list
        else:
            items = data["items"]
        
        results = [{"name": item.strip()} for item in items]  # Clean up spaces
        
        return jsonify(results), 200  # Send structured JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
    
