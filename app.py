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
    return jsonify(results=businesses)

@app.route('/api/search/<key>/<search>')
def get_by_zip(key, search):
    with open('scored_review.json') as f:
        businesses = (json.loads(f.readline()))
    in_zip = []
    if search != ' ':
        search_list = search.split(' ')
    else:
        search_list = [search]
    for val in businesses.values():
        res = val.get(key)
        if res is not None and search.lower() in res.lower():
            in_zip.append(val)
        if key.lower() == "zip":
            res = val.get('full_address')
            if any([x.lower() in res.lower() for x in search_list]):
                in_zip.append(val)
    return jsonify(results=in_zip)

if __name__ == '__main__':
    app.run(debug=True)