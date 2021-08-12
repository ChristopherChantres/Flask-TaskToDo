from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "chofo3mily"
app.config["MYSQL_DB"] = "flaskcontacts"
mysql = MySQL(app)

@app.route("/")
def Index():
    return "Hello Madafaka"


@app.route("/add_contact")
def add_contact():
    return "Agregar contacto"


@app.route("/edit")
def edit_contact():
    return "Editar contacto"


@app.route("/delete")
def delete_contact():
    return "Eliminar contacto"


if __name__ == "__main__":
    app.run(port = 3000, debug = True)