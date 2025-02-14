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
        print("Headers:", request.headers)
        print("Raw Data:", request.data)
        return jsonify({"error": "Content-Type must be application/json"}), 415  # Unsupported Media Type
    
    try:
        data = request.get_json()
    
        if not data or "items" not in data:
            return jsonify({"error": "Invalid request"}), 400
    
        results = []
        for item in data["items"]:
            results.append({
                "name": item,
                "status": "Checked",
            })

        return jsonify(results), 200  # Send structured JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
    
