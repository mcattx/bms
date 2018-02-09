from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('pages/index.html')


@app.route('/login')
def render_login():
    return render_template('pages/login.html')

@app.route('/admin')
def render_admin():
    return render_template('pages/admin.html')

if __name__ == '__main__':
    app.run(debug = True)
1
