from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}!"
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
