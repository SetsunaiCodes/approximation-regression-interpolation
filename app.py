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
        #Navbar Area
        html.Nav(
            id="navbar",
            className="flex flex-justify",
            children=[
                html.Div(
                    className="flex",
                    children=[
                        html.Img(
                            className="nav-image",
                            src="/assets/PlotSpaceLogo1.png"
                        ),
                        html.P(
                            'PlotSpace'
                        )
                    ]
                ),

            ]
        ),
        #Input Area
        html.Div(
            id="input-area",
            children=[
                html.Div(
                    className="container",
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
                )

            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className="flex",
                    children=[
                        #Graph Area
                         html.Div(
                             id="plot-container",
                             children=[
                                 #Anzeigen des Graphen
                                 dcc.Graph(
                                 className="container",
                                 id="linear-regression-plot"
                                 ),
                             ],
                         ),
                        #Meta Area
                        html.Div(
                         id="analyse-container",
                         children=[
                            html.Div(
                                className="container",
                                children=[
                                    html.P("Hier stehen Analytics")
                                ]
                            )
                         ],
                     ),
                   ]
                )
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
    fig.update_traces(marker=dict(color='rgb(62,177,178)', size=10),
                      selector=dict(mode='markers'))

    fig.update_traces(line=dict(color='rgb(116,227,152)', width=2),
                      selector=dict(mode='lines'))

    fig.update_layout(
                      xaxis_title="X-Achse",
                      yaxis_title="Y-Achse",
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      font=dict(family="Arial", size=12, color="white"),
                      xaxis=dict(gridcolor='rgb(65,67,85)'),
                      yaxis=dict(gridcolor='rgb(65,67,85)'))

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
