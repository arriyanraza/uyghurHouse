from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('guestbook.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/guestbook')
def guestbook():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries ORDER BY timestamp DESC')
    entries = cursor.fetchall()
    conn.close()
    return render_template('guestbook.html', entries=entries)

@app.route('/sign', methods=['POST'])
def sign_guestbook():
    name = request.form.get('name', '').strip()
    message = request.form.get('message', '').strip()
    website = request.form.get('website', '').strip()
    location = request.form.get('location', '').strip()
    
    if not name or not message:
        return "Name and message are required!", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO entries (name, message, website, location)
        VALUES (?, ?, ?, ?)
    ''', (name, message, website, location))
    conn.commit()
    conn.close()
    
    return redirect(url_for('guestbook'))

if __name__ == '__main__':
    app.run(debug=True)
