from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Required to use sessions

@app.route('/set/<name>')
def set_session(name):
    session['user'] = name
    return 'Session set!'

@app.route('/get')
def get_session():
    user = session.get('user')
    return f"User: {user}" if user else "No user in session."

if __name__ == '__main__':
    app.run(debug=True)
