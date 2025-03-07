# app.py
# using flask for testing 
from flask import Flask, request, jsonify, render_template
import subprocess
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # For testing purposes, return "it works"
    response = "it works"

    return jsonify({"response": response})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
