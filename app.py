from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS feedback (name TEXT, message TEXT)')
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('data.db')
    data = conn.execute('SELECT * FROM feedback').fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    msg = request.form['message']

    conn = sqlite3.connect('data.db')
    conn.execute('INSERT INTO feedback VALUES (?, ?)', (name, msg))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)