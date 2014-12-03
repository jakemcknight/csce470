__author__ = 'Miles Hickman'

from flask import Flask, render_template, abort, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bathroombuddy.html')

@app.route('/api/get_all')
def get_all_bathrooms():
    abort(418)

if __name__ == '__main__':
    app.run(debug=True)