from pandas_datareader import data

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from random import randint
import flask
import pandas as pd
import os
from datetime import datetime, timedelta

# %%
# server = flask.Flask('app')
# server.secret_key = os.environ.get('secret_key', 'secret')
#
# app = dash.Dash('app', server=server)

# app = dash.Dash()
# server = app.server
# app.config.suppress_callback_exceptions = True
#
#
# app.scripts.config.serve_locally = False
# dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'


# Setup the app

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

# Data
tickers = ['NVO', 'AMZN']
# Set period, number of days we are interested in prior to today
no_days = 30

now_minus_a_week = datetime.now() - timedelta(days = no_days)
start_date = str(now_minus_a_week.date())

#start_date = '2019-01-01'
#end_date = '2018-12-31'

#panel_data = data.DataReader(tickers, 'iex', start_date, end_date)
df = data.DataReader(tickers, 'iex', start = start_date); # Default of "end" is today
#panel_data = data.DataReader('F', 'robinhood')


app.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Novo Nordisk', 'value': 'NVO'},
            {'label': 'Amazon', 'value': 'AMZN'}
        ],
        value='AMZN',
        multi = False
    ),
    dcc.Graph(id='my-graph')
], className="container")

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    dff = df[selected_dropdown_value]
    return {
        'data': [{
            'x': list(dff.index),
            'y': list(dff.close),
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }

# Run the Dash app
if __name__ == '__main__':
    app.server.run()
