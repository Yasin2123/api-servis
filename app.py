from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API Calisiyor"

@app.route("/api/test")
def test():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()
