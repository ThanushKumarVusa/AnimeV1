from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db_connection
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "development-secret-key")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id, username FROM users
                   WHERE username = %s AND password = %s""",
                (username, password)
            )
            user = cursor.fetchone()
    finally:
        connection.close()

    if user:
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        return redirect(url_for("home"))

    return render_template("login.html", error="Invalid username or password")

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT title, genre, description FROM anime")
            anime_list = cursor.fetchall()
    finally:
        connection.close()

    return render_template("home.html", username=session["username"], anime_list=anime_list)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
