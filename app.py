###########################################
##### Import und Initialisierung ##########
###########################################

# Rechnungsimporte
import plotly.express as px
import random
import numpy as np

# Visualimporte
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import statsmodels.api as sm

#########################################
#### Daten und Funktionen definieren ####
#########################################

# Dictionary
data = {
    "X": [1, 2, 3, 4, 6, 4, 2],
    "Y": [2, 3, 5, 4, 6, 6, 7]
}

# Funktion um Daten für den Graphen zu generieren
def create_model(data):
    X = data["X"]
    X = sm.add_constant(X)
    Y = data["Y"]
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X)
    return model, predictions

# Funktion um zufällig Punkte zu generieren
def generate_random_points():
    new_data = {
        "X": [],
        "Y": []
    }
    #FIXME: manuell anpassbarer Wert für die Range in einem Input
    for i in range(10):
        x = random.uniform(0, 10)
        #FIXME: Min / Max Cap (Maxima und Minima der Sinus Kurve) sollte zufällig sein
        y = max(min(np.sin(x) + random.uniform(-0.5, 0.5), 1.5), -0.5) 

        ### Für den Unit Test der Funktion ###
        # Alte Zeie y = np.sin(x) + random.uniform(-0.5, 0.5) || Besteht Test 3 nicht, da y nicht zuverlässig im Intervall -0,5 - 1,5 landet
        # Neue Zeile y = max(min(np.sin(x) + random.uniform(-0.5, 0.5), 1.5), -0.5) || Besteht alle 3 Tests
        ######################################

        new_data["X"].append(x)
        new_data["Y"].append(y)
    return new_data

model, predictions = create_model(data)


# Externes Stylesheet für Font Awesome icons
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.config.serve_locally = True


###########################################
######### App-Layout generieren ###########
###########################################

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
                        html.Button(html.I(className="fas fa-trash"), id='delete-button', n_clicks=0, className='navbar-btn'),
                        html.Button(html.I(className="fas fa-plus"), id='add-button', n_clicks=0, className='navbar-btn'),
                        html.Button(html.I(className="fas fa-random"), id='generate-button', n_clicks=0, className='navbar-btn')
                    ]
                )
            ]
        ),
        html.Div(
            id="input-area",
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
            style={'margin-bottom': '20px', 'display': 'none'}  
        ),
        html.Div(
            className="flex flex-center",
            children=[
                dcc.Graph(
                    id="linear-regression-plot",
                    style={'width': '98vw', 'height': '90vh'}
                ),
            ],
        ),
    ],
)

###########################################
############# Callback Area ###############
###########################################

@app.callback(
    Output("input-area", "style"),
    [Input("add-button", "n_clicks"),
     Input("delete-button", "n_clicks")]
)
def toggle_input_area(add_clicks, delete_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return {'margin-bottom': '20px', 'display': 'none'}

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'add-button' and add_clicks % 2 == 1: 
        return {'margin-bottom': '20px', 'display': 'flex', 'justify-content': 'center','align-items': 'center', 'transition': 'opacity 0.5s ease-in-out', 'opacity': 1}
    elif button_id == 'delete-button' and delete_clicks > 0:
        return {'margin-bottom': '20px', 'display': 'none'}
    else:
        return {'margin-bottom': '20px', 'display': 'none'}

@app.callback(
    Output("linear-regression-plot", "figure"),
    [Input("submit-btn", "n_clicks"),
     Input("delete-button", "n_clicks"),
     Input("generate-button", "n_clicks")],
    [State("input_x", "value"),
     State("input_y", "value")]
)
def update_plot(submit_clicks, delete_clicks, generate_clicks, input_x, input_y):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit-btn' and submit_clicks > 0:
        if input_x is not None and input_y is not None:
            data["X"].append(input_x)
            data["Y"].append(input_y)

    elif button_id == 'delete-button' and delete_clicks > 0:
        data["X"] = []
        data["Y"] = []

    elif button_id == 'generate-button' and generate_clicks > 0:
        new_data = generate_random_points()
        data["X"] = new_data["X"]
        data["Y"] = new_data["Y"]

    if data["X"] and data["Y"]:
        model, predictions = create_model(data)

        fig = px.scatter(x=data["X"], y=data["Y"], trendline="ols")

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

    return fig if fig.data else px.scatter()

if __name__ == "__main__":
    app.run_server(debug=True)
