from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def home():
    return "Di2 - Eigen Docker webservice draait!"

@app.get("/api/status")
def status():
    return jsonify({
        "service": "Di2 eigen webservice",
        "status": "running",
        "time": datetime.now().isoformat()
    })

@app.get("/api/echo")
def echo():
    msg = request.args.get("msg", "geen_bericht")
    return jsonify({"echo": msg})

if __name__ == "__main__":
    # threaded=False om thread issues te vermijden op deze VM
    app.run(host="0.0.0.0", port=8081, threaded=False)
