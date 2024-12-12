from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """Home route."""
    return jsonify(message="Welcome to the Flask server!")

@app.route("/greet/<name>")
def greet(name):
    """Route to greet a person by name."""
    return jsonify(greeting=f"Hello, {name}!")

@app.route("/add", methods=["POST"])
def add_numbers():
    """Route to add two numbers."""
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if a is not None and b is not None:
        return jsonify(result=a + b)
    return jsonify(error="Please provide both 'a' and 'b' in the request body."), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
