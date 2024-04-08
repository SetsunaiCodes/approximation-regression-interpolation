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


app.layout = html.Div(
    [
        html.Div(
            id="input-area",
            children=[
                dcc.Input(
                    id="input_1",
                    type="text",
                    placeholder="input type 1",
                )
            ],
        ),
        html.Div(
            className="flex",
            children=[
                html.Div(
                    id="plot-container",
                    children=[
                        dcc.Graph(
                             id="linear-regression-plot"
                        ),
                    ],
                ),
                html.Div(
                    id="analyse-container",
                    children=[
                        html.P("Hier stehen Analytics")
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
