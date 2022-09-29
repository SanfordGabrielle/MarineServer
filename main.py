# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import flask
from flask import Flask, Response
from flask import Flask, render_template
from flask import request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=['POST', 'GET'])
def index():
    conn = get_db_connection()
    species = conn.execute('SELECT * FROM species').fetchall()
    conn.close()
    return render_template('home.html', species=species)


@app.route("/create", methods=['POST'])
def insertspecies():
    data = request.form
    conn = get_db_connection()
    query = f'INSERT INTO species (name, genus, max_age, region, average_size)' \
            f' VALUES (?, ?, ?, ?, ?)'

    data = list(data.values())
    conn.execute(query, data)

    conn.commit()
    conn.close()
    return Response("{'a':'b'}", status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run()
