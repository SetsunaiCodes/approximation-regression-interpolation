# Import und Initialisierung

# Rechnungsimports
import pandas as pd
import plotly.express as px

# Visualimports
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import statsmodels.api as sm

# Lese die Daten ein (temporäre Mock-Excel-Tabelle)
df = pd.read_csv("MockBook.csv", delimiter=";")

# Rechnungen über build in Rechenoperationen
X = df["X"]  # Unabhängige Variable
X = sm.add_constant(X)  # Konstante hinzufügen
Y = df["Y"]  # Abhängige Variable
model = sm.OLS(Y, X).fit()  # Lineare Regression
# Vorhersagen errechnen
predictions = model.predict(X)

# App-Layout erstellen
app = dash.Dash(__name__)

# Setze die externe CSS-Datei mit benutzerdefinierten Stilregeln
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# Initialisiere die Dash-App mit externen Stilen
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            style={"height": "18vh", "background-color": "red"},
            children=[
                dcc.Input(
                    id="input_1",
                    type="text",
                    placeholder="input type 1",
                )
            ],
        ),
        html.Div(
            style={"display": "flex"},
            children=[
                html.Div(
                    style={
                        "width": "80vw",
                        "height": "75vh",
                        "background-color": "blue",
                    },
                    children=[
                        dcc.Graph(id="linear-regression-plot"),
                    ],
                ),
                html.Div(
                    style={
                        "width": "20vw",
                        "height": "75vh",
                        "background-color": "green",
                    },
                    children=[
                        html.P("Hier stehen Analytics", style={"text-align": "center"})
                    ],
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
    fig = px.scatter(df, x="X", y="Y", trendline="ols")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
