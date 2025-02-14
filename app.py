from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for Webflow

# Load product data from CSV
def load_product_data():
    return pd.read_csv("products.csv")

@app.route("/check_products", methods=["POST"])
def check_products():
    data = request.json
    grocery_list = data.get("items", [])

    products_df = load_product_data()
    matched_products = products_df[products_df["product_name"].isin(grocery_list)]

    return jsonify(matched_products.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
