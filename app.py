from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "🚀 Hello! This is my first Flask web service."

# Dynamic greet route
@app.route("/greet/<name>")
def greet(name):
    return {"message": f"Hello, {name}! Welcome to Flask."}

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return {"result": a + b}
