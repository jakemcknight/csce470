__author__ = 'Miles Hickman'

from flask import Flask, render_template, abort, jsonify
from os import path
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bathroombuddy.html')

@app.route('/api/get_all')
def get_all_bathrooms():
    with open('scored_review.json') as f:
        businesses = (json.loads(f.readline()))
    return jsonify(businesses)

@app.route('/api/search/<key>/<search>')
def get_by_zip(key, search):
    with open('scored_review.json') as f:
        businesses = (json.loads(f.readline()))
    in_zip = []
    for val in businesses.values():
        res = val.get(key)
        if res is not None and search.lower() in res.lower():
            in_zip.append(val)
        if key.lower() == "zip":
            res = val.get('full_address')
            if search in res:
                in_zip.append(val)
    return jsonify(in_zip)

if __name__ == '__main__':
    app.run(debug=True)