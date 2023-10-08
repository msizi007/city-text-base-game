from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def login():
        return render_template("login.html")

@app.route("/display")
def display():
    name, password = request.form["username"], request.form["password"]
    return f"<p>Name: {name}, Password: {password}</p>"


app.run(debug=True)
