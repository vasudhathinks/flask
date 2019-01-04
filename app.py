from flask import Flask, render_template, request, redirect
import json
import requests
import pandas as pd


# Load key (Sort how to make private)
def load_key(key_file):
    with open(key_file) as json_data:
        keys_dict = json.load(json_data)
    return keys_dict['api_key']


app = Flask(__name__)

app.vars = {}
api_key = load_key('key.json')


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    return 'plot to be added'


@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(port=33507)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
