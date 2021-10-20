from flask import Flask, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4040)