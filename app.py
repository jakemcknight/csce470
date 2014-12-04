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

@app.route('/api/get_zip/<zip_code>')
def get_by_zip(zip_code):
    with open('scored_review.json') as f:
        businesses = (json.loads(f.readline()))
    in_zip = []
    for val in businesses.values():
        if zip_code in val["full_address"]:
            in_zip.append(val)
    return jsonify(results=in_zip)

if __name__ == '__main__':
    app.run(debug=True)