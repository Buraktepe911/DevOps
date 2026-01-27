from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()

    if not name:
        name = "anonymous"

    message = f"Hello {name}! You chose: {category if category else 'none'}"
    return render_template("result.html", name=name, category=category, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
