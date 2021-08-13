from flask import Flask, render_template, request, url_for, flash
from flask.globals import request
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

# Mysql connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "chofo3mily"
app.config["MYSQL_DB"] = "flaskcontacts"
mysql = MySQL(app)

# Settings
app.secret_key = "mysecretkey"

@app.route("/")
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    print(data)
    return render_template("index.html", contacts = data)


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


@app.route("/edit/<id>")
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE id = %s", (id))
    data = cur.fetchall()
    return render_template("edit_contact.html", contact = data[0])


@app.route("/update/<id>", methods = ["POST"])
def update_contact(id):
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET title = %s,
            description = %s,
            date = %s
        WHERE id = %s
        """, (title, description, date, id))
        mysql.connection.commit()
        flash("Contact update successfully")
        return redirect(url_for("Index"))



@app.route("/delete/<string:id>")
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("Task removed successfully")
    return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(port = 3000, debug = True)