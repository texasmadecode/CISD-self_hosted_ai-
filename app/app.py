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

    # Run Ollama model with user input
    # you can change model here by default it's mistral
    try:
        logging.debug(f"Running ollama with input: {user_input}")
        result = subprocess.run(["ollama", "run", "mistral", user_input], capture_output=True, text=True, check=True)
        response = result.stdout.strip()
        logging.debug(f"Ollama response: {response}")
    except subprocess.CalledProcessError as e:
        response = f"An error occurred: {e}"
        logging.error(response)

    return jsonify({"response": response})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
