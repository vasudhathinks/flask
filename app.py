from flask import Flask, render_template, request, redirect
import json
import io
import os
import requests
from datetime import datetime as dt, timedelta
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


# Load key (Sort how to make private)
def load_key(key_file):
    with open(key_file) as json_data:
        keys_dict = json.load(json_data)
    return keys_dict['api_key']


def plotter(symbol, types_list, key):
    end = dt.today().strftime("%Y-%m-%d")
    start = (dt.today() - timedelta(days=1000)).strftime("%Y-%m-%d")
    api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s/data.csv?api_key=%s&start_date=%s&end_date=%s' \
              % (symbol, key, start, end)

    session = requests.Session()
    data_request = session.get(api_url)
    data_df = pd.read_csv(io.StringIO(data_request.content.decode('utf-8')))
    data_df = data_df.set_index(pd.DatetimeIndex(data_df['Date']))

    fig = figure(title='Daily Prices over the last ~1,000 days/~3 years for ' + symbol,
                 plot_height=400, plot_width=600,
                 x_axis_label='Time', y_axis_label='Price',
                 x_axis_type='datetime')
    for price_type in types_list:
        fig.line(x=data_df.index, y=data_df[price_type].values, legend=price_type,
                 line_width=1, line_alpha=0.5)
    fig.legend.location = 'bottom_right'

    # show(fig)
    script, div = components(fig)
    return script, div


app = Flask(__name__)

app.vars = {}
api_key = load_key('key.json')


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/graph', methods=['POST'])
def graph():
    symbol = request.form['symbol']
    price_types = []
    if request.form.get('Open'):
        price_types.append('Open')
    if request.form.get('High'):
        price_types.append('High')
    if request.form.get('Low'):
        price_types.append('Low')
    if request.form.get('Close'):
        price_types.append('Close')

    app.vars['symbol'] = symbol.upper()
    app.vars['types'] = price_types
    print(app.vars['symbol'], app.vars['types'])

    script, div = plotter(app.vars['symbol'], app.vars['types'], api_key)
    return render_template('graph.html', script=script, div=div)
    # return 'plot to be added'


@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(port=33507)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    # app.run()
