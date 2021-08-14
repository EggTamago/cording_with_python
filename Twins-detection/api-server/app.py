from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from werkzeug.utils import secure_filename
import pykakasi
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'success'

@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload():
    if request.method == 'GET':
        return 
    elif request.method == 'POST':
        print("---------------------------------------")
        print(vars(request))
        print()
        file = request.files['image']
        save_filename = secure_filename(file.filename)
        file.save(os.path.join('./images', save_filename))
        return 'get file !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4040)