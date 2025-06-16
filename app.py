from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'hotels.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()

@app.route('/')
def index():
    db = get_db()
    hotels = db.execute('SELECT * FROM hotels').fetchall()
    return render_template('index.html', hotels=hotels)

@app.route('/hotel/<int:hotel_id>')
def hotel(hotel_id):
    db = get_db()
    hotel = db.execute('SELECT * FROM hotels WHERE id = ?', (hotel_id,)).fetchone()
    menu = db.execute('SELECT * FROM menu WHERE hotel_id = ?', (hotel_id,)).fetchall()
    return render_template('hotel.html', hotel=hotel, menu=menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
