from flask import Flask
import pymongo
import elasticsearch
import elasticsearch_dsl
import mongoengine

app = Flask(__name__)
print(pymongo.__version__)
print(elasticsearch.__version__)
print(elasticsearch_dsl.__version__)
print(mongoengine.__version__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=12345, host='0.0.0.0')
