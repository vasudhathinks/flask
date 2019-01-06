### Welcome to the enigmatic-ridge-47092 repo!

###### About
[enigmatic-ridge-47092](http://enigmatic-ridge-47092.herokuapp.com/index) is a 
Flask app on Heroku that returns the daily stock prices over the last ~1,000 days 
for a given stock ticker/symbol as sourced from [Quandl](https://www.quandl.com/). 

###### Try It Out
Visit [enigmatic-ridge-47092](http://enigmatic-ridge-47092.herokuapp.com/index) to 
give it a try!

###### Create Your Own
To set up this app:
1. Clone this repo. `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
1. To access this dataset, [Quandl](https://www.quandl.com/)'s WIKI Prices, 
[set up an account](https://www.quandl.com/databases/WIKIP/usage/quickstart/api) 
to get an API key. 
1. To run locally, create a file in your local repo called `.env` (which is and 
should be included in `.gitignore`) that contains:
     ```
     export quandl_key=<your api key>
     ```
     `quandl_key` can be called something else, but that is how it is referenced in `app.py` )  
1. To run locally, create and activate your virtual environment (to import Flask, etc.) and run:
     ```commandline
     source .env
     python app.py
     ```  
1. To run on Heroku, add your `quandl_key` to `Config Vars`. 


###### Additional Info
- For Heroku, check out this guide for using the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python).
- When creating the app with `heroku create`, use 
  ```
  heroku create --buildpack https://github.com/thedataincubator/conda-buildpack.git#py3
  ```