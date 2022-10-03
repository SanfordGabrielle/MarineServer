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


@app.route("/", methods=['POST', 'GET', 'DELETE'])
def index():
    conn = get_db_connection()
    species = conn.execute('SELECT * FROM species').fetchall()
    conn.close()
    return render_template('home.html', species=species)


@app.route("/create", methods=['POST'])
def insertspecies():
    conn = get_db_connection()
    form = request.form
    data = list(form.values())

    query = f'INSERT INTO species (name, genus, max_age, region, average_size)' \
            f'VALUES (?, ?, ?, ?, ?)'
    conn.execute(query, data)

    conn.commit()
    conn.close()
    return Response("{'a':'b'}", status=201, mimetype='application/json')


@app.route("/update", methods=['POST'])
def updatespecies():
    conn = get_db_connection()
    form = request.form
    data = list(form.values())

    query = f'UPDATE species SET genus = ?, max_age = ?, region = ?, average_size = ? WHERE name = ?'
    conn.execute(query, (data[1], data[2], data[3], data[4], data[0]))

    conn.commit()
    conn.close()
    return Response("{'a':'b'}", status=201, mimetype='application/json')


@app.route("/delete", methods=['POST'])
def deletespecies():
    conn = get_db_connection()
    form = request.form
    data = list(form.values())

    query = f'DELETE FROM species WHERE name = ?'
    conn.execute(query, (data[0],))

    conn.commit()
    conn.close()
    return Response("{'a':'b'}", status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run()
