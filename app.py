from flask import Flask
import pymongo
import mongoengine

app = Flask(__name__)
print(pymongo.__version__)
print(mongoengine.__version__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=12345, host='0.0.0.0')
