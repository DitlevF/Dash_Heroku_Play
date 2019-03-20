import dash
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime, timedelta
import webbrowser

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
} # Dictionary

app.layout = html.Div(style = {'backgroundColour': colors['background']}, children = [
    html.H1(children = 'Hello Dash',
    style = {
    'textAlign': 'center',
    'color': colors['text']
    }
    ),

    html.Div(children = '''Dash: A web application framework for Python.''', style = {
        'textAlign': 'center',
        'color': colors['text']
        }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [10, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [10, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


if __name__ == '__main__':
    #webbrowser.open('http://127.0.0.1:8050/', new=0) # Open webbrowser in current browser, new = 0
    app.run_server(debug=True)
