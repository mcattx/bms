from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Here is Home page.'


@app.route('/login')
def render_login():
    return 'Here is Login Page.'


@app.route('/admin')
def render_admin():
    return 'Here is admin page.'


if __name__ == '__main__':
    app.run(debug = True)
