import io
import requests
import pandas as pd
from datetime import datetime as dt, timedelta
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

end = dt.today().strftime("%Y-%m-%d")
start = (dt.today() - timedelta(days=1000)).strftime("%Y-%m-%d")
print(start, end)

stock = 'AAPL'
key = 'j486HwgjV_pd-meJgiFC'
api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s/data.csv?api_key=%s&start_date=%s&end_date=%s' \
          % (stock, key, start, end)
session = requests.Session()
data_request = session.get(api_url)

# print(data_request.status_code)
# print(len(data_request.content))
# print(data_request.content)

data_df = pd.read_csv(io.StringIO(data_request.content.decode('utf-8')))
# print(data_df.head())

# static_data = pd.read_csv('sample.csv')
# print(static_data.head())

data_df = data_df.set_index(pd.DatetimeIndex(data_df['Date']))
# print(data_df.head())

fig = figure(title='Stock Prices over the last ~1,000 days/~3 years:',
             plot_height=600, plot_width=600,
             x_axis_label='Date', y_axis_label='Price',
             x_axis_type='datetime')

fig.line(x=data_df.index, y=data_df['Open'].values, legend='Open',
         line_width=1, line_alpha=0.5)

show(fig)
