### Welcome to the Repo for enigmatic-ridge-47092

###### About
[enigmatic-ridge-47092](http://enigmatic-ridge-47092.herokuapp.com/index) is a 
Flask app on Heroku that returns the daily stock prices over the last ~1,000 days 
for a given stock ticker/symbol as sourced from [Quandl](https://www.quandl.com/). 

###### Try It Out
Visit [enigmatic-ridge-47092](http://enigmatic-ridge-47092.herokuapp.com/index) to 
give it a try!

###### Create Your Own
To set up this app or something similar for yourself, follow these steps:
1. Clone this repo. The app is self contained with 3 pages as shown in `templates/`.
1. To run locally, create a file 

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate HTML in `templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the [conda buildpack](https://github.com/thedataincubator/conda-buildpack).
  If you choose not to, put all requirements into `requirements.txt`

  `heroku config:add BUILDPACK_URL=https://github.com/thedataincubator/conda-buildpack.git#py3`

  The advantages of conda include easier virtual environment management and fast package installation from binaries (as compared to the compilation that pip-installed packages sometimes require).
  One disadvantage is that binaries take up a lot of memory, and the slug pushed to Heroku is limited to 300 MB. Another note is that the conda buildpack is being deprecated in favor of a Docker solution (see [docker branch](https://github.com/thedataincubator/flask-framework/tree/docker) of this repo for an example).
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
