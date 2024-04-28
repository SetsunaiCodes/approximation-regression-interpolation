# Import und Initialisierung

# Rechnungsimports
import pandas as pd
import plotly.express as px

# Visualimports
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import statsmodels.api as sm

# Definiere deine Daten als Dictionary
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 3, 5, 4, 6]
}

# Verwende das Dictionary in deinem Code
X = data["X"]  # Unabhängige Variable
X = sm.add_constant(X)  # Konstante hinzufügen
Y = data["Y"]  # Abhängige Variable
model = sm.OLS(Y, X).fit()  # Lineare Regression
# Vorhersagen errechnen
predictions = model.predict(X)

# App-Layout erstellen
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        #Input Area - DIE STEHT AKTUELL AUF DISPLAY NONE
        html.Div(
            id="input-area",
            children=[
                #Input + Button um neuen Punkt hinzuzufügen
                dcc.Input(
                    id="input_1",
                    type="text",
                    className="input-area-input",
                    placeholder="input type 1",
                ),
                html.Button(
                    'Add',
                    className="submit-btn"
                )
            ]
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

# Callback erstellen, damit der Plot aktualisiert werden kann
@app.callback(
    Output("linear-regression-plot", "figure"),
    [Input("input_1", "value")],
)
def update_plot(input_value):
    # Generieren des Plots
    fig = px.scatter(x=data["X"], y=data["Y"], trendline="ols")

    # Styling des Graphen
    fig.update_traces(marker=dict(color='rgb(255,0,0)', size=10),
                      selector=dict(mode='markers'))

    fig.update_traces(line=dict(color='rgb(0,0,255)', width=2),
                      selector=dict(mode='lines'))

    fig.update_layout(
                      xaxis_title="X-Achse",
                      yaxis_title="Y-Achse",
                      plot_bgcolor='rgba(255, 255, 255, 1)',
                      paper_bgcolor='rgba(255, 255, 255, 1)',
                      font=dict(family="Arial", size=12, color="black"),
                      xaxis=dict(gridcolor='rgb(128,128,128)'),
                      yaxis=dict(gridcolor='rgb(128,128,128)'))

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
