# | Import und Initialisierung |
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import statsmodels.api as sm

# Lese die Daten ein (temporäre Mock-Excel-Tabelle)
df = pd.read_csv("MockBook.csv", delimiter=";")


# | Rechnungen über build in Rechenoperationen |
X = df["X"]  # Unabhängige Variable
X = sm.add_constant(X)  # Konstante hinzufügen
Y = df["Y"]  # Abhängige Variable
model = sm.OLS(Y, X).fit()  # Lineare Regression
# Vorhersagen berrechnen
predictions = model.predict(X)

# | App-Layout erstellen |
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Linear Regression Plot", style={"text-align": "center"}),
        dcc.Graph(id="linear-regression-plot"),
    ]
)

# | Callback erstellen, damit der Plot aktualisiert werden kann |
@app.callback(
    Output("linear-regression-plot", "figure"),
    [Input("linear-regression-plot", "id")],
)
def update_plot(id):
    # Generieren des Plots
    fig = px.scatter(df, x="X", y="Y", trendline="ols")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
