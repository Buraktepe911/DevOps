from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "J1 Jenkins Pipeline OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, threaded=False)
