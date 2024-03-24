from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def aboutpage():
    return "about"


@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id=?',(id,))
    pizza = cur.fetchall()
    return render_template('pizza.html', pizza=pizza)


if __name__ == "__main__":  # Last lines
    app.run(debug=True)
