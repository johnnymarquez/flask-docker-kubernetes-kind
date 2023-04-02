from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    A simple webservice
    """
    return 'Hello from Python!'


if __name__ == '__main__':
    # Run on local host
    app.run(host='0.0.0.0')
