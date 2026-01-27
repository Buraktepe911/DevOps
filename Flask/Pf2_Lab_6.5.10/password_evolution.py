import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
db_name = "test.db"

# ---------- DB helpers ----------
def create_tables():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Phase 2: Plaintext table (onveilig)
    c.execute("""
        CREATE TABLE IF NOT EXISTS users_plaintext (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    # Phase 3: Hashed table (veiliger)
    c.execute("""
        CREATE TABLE IF NOT EXISTS users_hashed (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------- Plaintext functions ----------
def user_exists_plain(username):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT username FROM users_plaintext WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    return row is not None

def create_user_plain(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO users_plaintext (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def check_login_plain(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT password FROM users_plaintext WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    return row[0] == password


# ---------- Hash helpers (Phase 3) ----------
def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def user_exists_hashed(username):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT username FROM users_hashed WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    return row is not None

def create_user_hashed(username, password):
    pw_hash = sha256_hash(password)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO users_hashed (username, password_hash) VALUES (?, ?)", (username, pw_hash))
    conn.commit()
    conn.close()

def check_login_hashed(username, password):
    pw_hash = sha256_hash(password)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users_hashed WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    stored_hash = row[0]
    return stored_hash == pw_hash


# ---------- Routes ----------
@app.route("/")
def index():
    return "Pf2 - Password evolution is running! (Phase 2 plaintext + Phase 3 hashed)"


# Phase 2: Signup/Login (plaintext)
@app.route("/signup_plaintext", methods=["POST"])
def signup_plaintext():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not username or not password:
        return "ERROR: username and password required", 400
    if user_exists_plain(username):
        return "ERROR: user already exists (plaintext)", 409

    create_user_plain(username, password)
    return "OK: user created (plaintext)", 201


@app.route("/login_plaintext", methods=["POST"])
def login_plaintext():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not username or not password:
        return "ERROR: username and password required", 400

    if check_login_plain(username, password):
        return "OK: login success (plaintext)", 200
    return "ERROR: login failed (plaintext)", 401


# Phase 3: Signup/Login (hashed)
@app.route("/signup_hashed", methods=["POST"])
def signup_hashed():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not username or not password:
        return "ERROR: username and password required", 400
    if user_exists_hashed(username):
        return "ERROR: user already exists (hashed)", 409

    create_user_hashed(username, password)
    return "OK: user created (hashed)", 201


@app.route("/login_hashed", methods=["POST"])
def login_hashed():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not username or not password:
        return "ERROR: username and password required", 400

    if check_login_hashed(username, password):
        return "OK: login success (hashed)", 200
    return "ERROR: login failed (hashed)", 401


if __name__ == "__main__":
    create_tables()
    # HTTPS (self-signed) zoals in het lab
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
