from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/user')
def hello(name=Mateusz):
    return render_template('hello.html', name=name)
