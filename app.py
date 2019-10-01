import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Pick breakfast'
tabtitle = 'brekkie!'
list_of_breakfast=['yogurt', 'donuts', 'cereal']
list_of_numbers=['one', 'two', 'three']
sourceurl = 'https://dash.plot.ly/getting-started-part-2'
githublink = 'https://github.com/regina-avila/dash-callbacks-multi-input'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id='pick-a-color',
                options=[
                        {'label':list_of_breakfast[0], 'value':list_of_breakfast[0]},
                        {'label':list_of_breakfast[1], 'value':list_of_breakfast[1]},
                        {'label':list_of_breakfast[2], 'value':list_of_breakfast[2]},
                        ],
#this is the default value
                value='choose',
                ),
        ],className='two columns'),
        html.Div([
            dcc.RadioItems(
                id='pick-a-number',
                options=[
                        {'label':list_of_numbers[0], 'value':list_of_numbers[0]},
                        {'label':list_of_numbers[1], 'value':list_of_numbers[1]},
                        {'label':list_of_numbers[2], 'value':list_of_numbers[2]},
                        ],
                value='one',
                ),
        ],className='two columns'),
        html.Div([
            html.Div(id='your_output_here', children=''),
        ],className='eight columns'),
    ],className='twelve columns'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback

@app.callback(Output('your_output_here', 'children'),
              [Input('pick-a-breakfast', 'value'),
               Input('pick-a-number', 'value')])
def radio_results(breakfast_you_picked, number_you_picked):
    image_you_chose=f'{breakfast_you_picked}-{number_you_picked}.jpg'
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),

############ Deploy
if __name__ == '__main__':
    app.run_server()
