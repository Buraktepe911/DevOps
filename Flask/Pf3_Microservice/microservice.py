from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Pf3 - Eigen Flask microservice draait!"

@app.route("/status")
def status():
    return jsonify({
        "service": "Pf3 microservice",
        "status": "running"
    })

@app.route("/info")
def info():
    return jsonify({
        "name": "Pf3 eigen microservice",
        "version": "1.0",
        "author": "DevOps student"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
