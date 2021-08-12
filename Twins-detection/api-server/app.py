from flask import Flask, request
from werkzeug.utils import secure_filename
import pykakasi
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return 
    elif request.method == 'POST':
        file = request.file['file']
        save_filename = secure_filename(file.filename)
        file.save(os.path.join('./images', save_filename))
        return 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ports=4040)