from flask import Flask, request, render_template_string, g
import sqlite3

app = Flask(__name__)
DATABASE = 'flag.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor = get_db().execute(query)
        result = cursor.fetchone()
        if result:
            return f"<h1>Welcome {username}!</h1><p>Flag: {result[3]}</p>"
        else:
            message = 'Invalid credentials'
    return render_template_string('''
        <h1>Login</h1>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{message}}</p>
    ''', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
