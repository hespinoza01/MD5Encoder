from flask import Flask, request, url_for, redirect
from md5Encode import md5Encode
from console import console
from jsonResponse import jsonResponse
from datetime import datetime

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(err):
    console.error("Error: {}. \nUrl: {}. Redirecting to index.".format(err, request.url))
    return redirect(url_for('index'))

@app.route('/md5encoder/api/')
@app.route('/md5encoder/api/<data>')
@jsonResponse
def index(data=""):
    JSON = {}
    JSON['date'] = str(datetime.now())
    JSON['data'] = md5Encode('hola') if data != "" else "Sorry! We don't receive data to encode"
    return JSON

if __name__ == '__main__':
    app.run(
        debug=True
    )