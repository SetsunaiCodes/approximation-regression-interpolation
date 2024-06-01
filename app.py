###########################################
##### Import und Initialisierung ##########
###########################################

# Rechnungsimports
import pandas as pd
import plotly.express as px

# Visualimports
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import statsmodels.api as sm

###########################################
############ Daten definieren #############
###########################################

# Dictionary
data = {
    "X": [1, 2, 3, 4, 6, 4, 2],
    "Y": [2, 3, 5, 4, 6, 6, 7]
}

def create_model(data):
    X = data["X"]
    X = sm.add_constant(X)
    Y = data["Y"]
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X)
    return model, predictions

model, predictions = create_model(data)

###########################################
######### App-Layout generieren ###########
###########################################

app = dash.Dash(__name__)
app.css.config.serve_locally = True

app.layout = html.Div(
    [
        html.Nav(
            className="navbar",
            children=[
                html.Button('-', id='delete-button', n_clicks=0, className='navbar-btn'),
                html.Button('+', id='add-button', n_clicks=0, className='navbar-btn')
            ]
        ),
        html.Div(
            id="input-area",
            children=[
                html.Button('×', id='close-button', n_clicks=0, className='close-btn'),
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
                    'Add',
                    id="submit-btn",
                    n_clicks=0,
                    className='submit-btn'
                ),
            ],
            # Standardmäßig display: none | Eingefahren / OnClick: display: inherit | Ausgefahren
            style={'margin-bottom': '20px', 'display': 'none'}  
        ),
        # Graph Area
        html.Div(
            className="flex flex-center",
            children=[
                # Anzeigen des Graphen
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
     Input("close-button", "n_clicks")]
)
def toggle_input_area(add_clicks, close_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return {'margin-bottom': '20px', 'display': 'none'}

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'add-button' and add_clicks > 0:
        return {'margin-bottom': '20px', 'display': 'block', 'transition': 'opacity 0.5s ease-in-out', 'opacity': 1}
    elif button_id == 'close-button' and close_clicks > 0:
        return {'margin-bottom': '20px', 'display': 'none'}
    else:
        return {'margin-bottom': '20px', 'display': 'none'}

@app.callback(
    Output("linear-regression-plot", "figure"),
    [Input("submit-btn", "n_clicks"),
     Input("delete-button", "n_clicks")],
    [State("input_x", "value"),
     State("input_y", "value")]
)
def update_plot(submit_clicks, delete_clicks, input_x, input_y):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit-btn' and submit_clicks > 0:
        if input_x is not None and input_y is not None:
            data["X"].append(input_x)
            data["Y"].append(input_y)

    elif button_id == 'delete-button' and delete_clicks > 0:
        data["X"] = []
        data["Y"] = []

    if data["X"] and data["Y"]:  # Check ob die Data Arrays nicht leer sind
        model, predictions = create_model(data)

        fig = px.scatter(x=data["X"], y=data["Y"], trendline="ols")

        fig.update_traces(marker=dict(color='rgb(70, 130, 180)', size=10),  # Anpassung der Punktfarbe
                          selector=dict(mode='markers'))

        fig.update_traces(line=dict(color='rgb(30, 144, 255)', width=4),  # Anpassung der Linienfarbe
                          selector=dict(mode='lines'))

        fig.update_layout(
                          xaxis_title="X-Achse",
                          yaxis_title="Y-Achse",
                          plot_bgcolor='rgba(255, 255, 255, 1)',
                          paper_bgcolor='rgba(255, 255, 255, 1)',
                          font=dict(family="Arial", size=12, color="rgb(88,88,88)"),
                          xaxis=dict(gridcolor='rgb(211,211,211)'),  
                          yaxis=dict(gridcolor='rgb(211,211,211)'))

    else:
        fig = px.scatter()  

    return fig if fig.data else px.scatter()

if __name__ == "__main__":
    app.run_server(debug=True)
