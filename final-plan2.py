################################
########### Imports ############
################################

import random
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from equation import regress, regress2, interpolate


# Data Object
data = {
    "X": [1, 2, 3, 4, 5, 6, 7],
    "Y": [2, 3, 5, 4, 6, 6, 7]
}

#########################################################
## Func um die lineare Regression manuell zu berechnen ##
#########################################################

def calculate_manual_regression(data):
    X = np.array(data["X"])
    Y = np.array(data["Y"])
    n = len(X)
    
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_X2 = np.sum(X ** 2)
    
    nenner = n * sum_X2 - sum_X ** 2
    if nenner == 0:
        #Nenner meint hier den obere Bereich der Ausgangsfunktion
        #Edgecase
        raise ValueError("Der Nenner ist 0. Regression kann nicht berechnet werden.")
    
    a = (n * sum_XY - sum_X * sum_Y) / nenner
    b = (sum_Y * sum_X2 - sum_X * sum_XY) / nenner
    
    return a, b

# Func um random Punkte zu generiern
def generate_random_points():
    new_data = {"X": [], "Y": []}
    for _ in range(10):
        x = random.uniform(0, 10)
        y = max(min(np.sin(x) + random.uniform(-0.5, 0.5), 1.5), -0.5)
        new_data["X"].append(x)
        new_data["Y"].append(y)
    return new_data

# Externes Stylesheet Font Awesome
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.config.serve_locally = True

################################
########### App Layout #########
################################

app.layout = html.Div(
    [
        html.Nav(
            className="navbar",
            children=[
                html.Div(
                    id="logo-container",
                    children=[
                        html.Img(src="assets/SionLogo.png", alt="Sion Logo", className="branding")
                    ]
                ),
                html.Div(
                    id="nav-button-container",
                    children=[
                        html.Button(html.I(className="fas fa-list"), id='toggle-list-button', n_clicks=0, className='navbar-btn-secondary'),
                        html.Button(html.I(className="fas fa-random"), id='generate-button', n_clicks=0, className='navbar-btn-secondary'),
                        html.Button(html.I(className="fas fa-trash"), id='clear-button', n_clicks=0, className='navbar-btn-secondary'),
                        html.Button(html.I(className="fas fa-plus"), id='add-button', n_clicks=0, className='navbar-btn')
                    ]
                )
            ]
        ),
        html.Div(
            id="input-area",
            className='',
            children=[
                dcc.Input(
                    id="input_x",
                    type="number",
                    placeholder="X-Wert",
                    className='input-area-input'
                ),
                dcc.Input(
                    id="input_y",
                    type="number",
                    placeholder="Y-Wert",
                    className='input-area-input'
                ),
                html.Button(
                    [html.I(className="fas fa-check"), " Add"],
                    id="submit-btn",
                    n_clicks=0,
                    className='submit-btn'
                ),
            ],
            style={'display': 'none'}
        ),
        
        dcc.Tabs(id="tabs", value='tab-1', className="custom-tabs", children=[
            dcc.Tab(label='Regression', value='tab-1',className='custom-tab',selected_className='custom-tab--selected'),
            dcc.Tab(label='Interpolation', value='tab-2',className='custom-tab',selected_className='custom-tab--selected'),
        ]),
        
        html.Div(
            className="flex flex-center",
            id="presentation-container",
            children=[
                html.Div(
                    className="margin-container",
                    children=[]
                ),
                dcc.Graph(
                    id="plot",
                    style={'width': '70vw', 'height': '80vh'}
                ),
                html.Div(
                    id="margin-container",
                    className="margin-container",
                    children=[
                        html.Div(
                            id="point-list",
                            className="point-list",
                            children=[],
                            style={'display': 'none'}
                        )
                    ]
                ),
            ],
        ),
    ],
)

################################
########### Callbacks ##########
################################


# Toggle input area display
@app.callback(
    Output("input-area", "style"),
    [Input("add-button", "n_clicks")]
)
def toggle_input_area_display(add_clicks):
    if add_clicks % 2 == 1:
        return {'display': 'flex'}
    return {'display': 'none'}

# Toggle input area animation
@app.callback(
    Output("input-area", "className"),
    [Input("add-button", "n_clicks")]
)
def toggle_input_area_animation(add_clicks):
    if add_clicks % 2 == 1:
        return 'show'
    return ''

# Toggle point list display
@app.callback(
    Output("point-list", "style"),
    [Input("toggle-list-button", "n_clicks")]
)
def toggle_point_list_display(toggle_clicks):
    if toggle_clicks % 2 == 1:
        return {'display': 'block'}
    return {'display': 'none'}

# Update plot und point list
@app.callback(
    Output("plot", "figure"),
    Output("point-list", "children"),
    [Input("submit-btn", "n_clicks"),
     Input("generate-button", "n_clicks"),
     Input("clear-button", "n_clicks"),
     Input("tabs", "value")],
    [State("input_x", "value"),
     State("input_y", "value")]
)
def update_plot(submit_clicks, generate_clicks, clear_clicks, tab, input_x, input_y):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit-btn' and submit_clicks > 0:
        if input_x is not None and input_y is not None:
            data["X"].append(input_x)
            data["Y"].append(input_y)

    elif button_id == 'generate-button' and generate_clicks > 0:
        new_data = generate_random_points()
        data["X"] = new_data["X"]
        data["Y"] = new_data["Y"]

    elif button_id == 'clear-button' and clear_clicks > 0:
        data["X"] = []
        data["Y"] = []

    if data["X"] and data["Y"]:
        X = np.array(data["X"])
        Y = np.array(data["Y"])



        if tab == 'tab-1':
            werteX, werteY = regress2(data)
            #regression_line = a * X + b
            fig = px.scatter(x=X, y=Y)
            fig.add_scatter(x=werteX, y=werteY, mode='lines', name='Line')
        elif tab == 'tab-2':
            werteX, werteY = interpolate(data)
            fig = px.scatter(x=X, y=Y)
            fig.add_scatter(x=werteX, y=werteY, mode='lines', name='Line')

        fig.update_traces(marker=dict(color='rgb(15, 91, 152)', size=10),
                          selector=dict(mode='markers'))

        fig.update_traces(line=dict(color='rgb(10, 140, 247)', width=4),
                          selector=dict(mode='lines'))

        fig.update_layout(
            xaxis_title="X-Achse",
            yaxis_title="Y-Achse",
            plot_bgcolor='rgba(247, 247, 247, 1)',
            paper_bgcolor='rgba(247, 247, 247, 1)',
            font=dict(family="Arial", size=12, color="rgb(88,88,88)"),
            xaxis=dict(gridcolor='rgb(211,211,211)'),
            yaxis=dict(gridcolor='rgb(211,211,211)'))

    else:
        fig = px.scatter()

    point_list_children = []
    for x, y in zip(data["X"], data["Y"]):
        point_list_children.append(
            html.Div(
                className="point-item",
                children=[
                    html.Span(f"({x}, {y})")
                ]
            )
        )

    return fig if fig.data else px.scatter(), point_list_children

if __name__ == "__main__":
    app.run_server(debug=False)
