from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import pykakasi
import os

import sys
sys.path.append('../')
from ai import inference

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
        for id, file in request.files.items():
            file = request.files[str(id)]
            # save_filename = secure_filename(file.filename)
            save_filename = id + '.jpg'
            file.save(os.path.join('../ai/images', save_filename))

        inference_result = inference.infer()

        return inference_result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4040)