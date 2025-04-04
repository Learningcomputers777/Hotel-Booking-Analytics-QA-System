from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Load environment variables or set default FastAPI URL
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000/ask")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/query", methods=["GET"])
def query():
    user_query = request.args.get("query")  # Get query from URL
    response = requests.get(FASTAPI_URL, params={"query": user_query})  # Send query to FastAPI backend

    if response.status_code == 200:
        return jsonify({"answer": response.json().get("answer", "No valid response received.")})
    else:
        return jsonify({"answer": "Error: No valid response received."})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
