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

app.layout = html.Div(
    [
        html.Div(
            id="input-area",
            children=[
                dcc.Input(
                    id="input_x",
                    type="number",
                    placeholder="X-Wert",
                ),
                dcc.Input(
                    id="input_y",
                    type="number",
                    placeholder="Y-Wert",
                ),
                html.Button(
                    'Add',
                    id="submit-btn",
                    n_clicks=0
                ),
                html.Div(
                    id="current-points",
                    style={'margin-top': '20px'}
                ),
            ],
            style={'margin-bottom': '20px'}
        ),
        #Graph Area
        html.Div(
            className="flex flex-center",
            children=[
                #Anzeigen des Graphen
                dcc.Graph(
                    id="linear-regression-plot",
                    style={'width': '98vw', 'height': '98vh'}
                ),
            ],
        ),
    ],
)


###########################################
############# Callback Area ###############
###########################################

@app.callback(
    [Output("linear-regression-plot", "figure"),
     Output("current-points", "children")],
    [Input("submit-btn", "n_clicks")],
    [State("input_x", "value"),
     State("input_y", "value")]
)
def update_plot(n_clicks, input_x, input_y):
    if n_clicks > 0 and input_x is not None and input_y is not None:
        data["X"].append(input_x)
        data["Y"].append(input_y)

    model, predictions = create_model(data)

    fig = px.scatter(x=data["X"], y=data["Y"], trendline="ols")

    fig.update_traces(marker=dict(color='rgb(239, 115, 112)', size=10),
                      selector=dict(mode='markers'))

    fig.update_traces(line=dict(color='rgb(140, 116, 231)', width=4),
                      selector=dict(mode='lines'))

    fig.update_layout(
                      xaxis_title="X-Achse",
                      yaxis_title="Y-Achse",
                      plot_bgcolor='rgba(255, 255, 255, 1)',
                      paper_bgcolor='rgba(255, 255, 255, 1)',
                      font=dict(family="Arial", size=12, color="rgb(88,88,88)"),
                      xaxis=dict(gridcolor='rgb(211,211,211)'),  
                      yaxis=dict(gridcolor='rgb(211,211,211)'))  

    current_points = [f"({x}, {y})" for x, y in zip(data["X"], data["Y"])]
    current_points_display = html.Ul([html.Li(point) for point in current_points])

    return fig, current_points_display

# Command um den Flask Server zu starten
if __name__ == "__main__":
    app.run_server(debug=True)
