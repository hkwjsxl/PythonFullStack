from flask import Flask

app = Flask(__name__)


@app.route('//')
def home():
    return 'Welcome Flask'


@app.route('/index/')
def index():
    return 'Hello Flask'


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
