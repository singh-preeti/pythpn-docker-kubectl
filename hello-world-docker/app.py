# This is a sample Python script.

from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def print_hello(name):
    return 'Hello ,%s' % name


if __name__ == '__main__':
    app.run()
