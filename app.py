from flask import Flask, render_template, request, url_for, flash
from flask.globals import request
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "chofo3mily"
app.config["MYSQL_DB"] = "flaskcontacts"
mysql = MySQL(app)

@app.route("/")
def Index():
    return render_template("index.html")


@app.route("/add_task", methods = ["POST"])
def add_contact(): 
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (title, description, date) VALUES (%s, %s, %s)", (title, description, date))
        mysql.connection.commit()
        flash("Task added successfully")

        return redirect(url_for("Index"))


@app.route("/edit")
def edit_contact():
    return "Editar contacto"


@app.route("/delete")
def delete_contact():
    return "Eliminar contacto"


if __name__ == "__main__":
    app.run(port = 3000, debug = True)