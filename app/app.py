# app.py
#using flask for testing 
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Run Ollama model with user input
    #you can change model here
    result = subprocess.run(["ollama", "run", "mistral", user_input], capture_output=True, text=True)
    
    return jsonify({"response": result.stdout.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
