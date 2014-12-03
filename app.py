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
    businesses = []
    with open(path.join('NaiveBayes','bathroom_business.json')) as f:
        for line in f:
            businesses.append(json.loads(line))
    return jsonify(results=businesses)

if __name__ == '__main__':
    app.run(debug=True)