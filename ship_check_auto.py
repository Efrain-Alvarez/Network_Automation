##################################################
#Automation of Ship Check
#11/17/2024
#Efrain Alvarez
##################################################

import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px


df = pd.read_csv("./customers-100.csv")

app = Dash(__name__)

app.layout = [
    html.H1(children = "REAP PING", style={'textAlign':'center', 'color': '#4248a9'}),
    dcc.Dropdown(
        options = [{'label':name, 'value':name} for name in df["First Name"].unique()],
        value = df["First Name"].iloc[0]
    )
]

if __name__ == '__main__':
    app.run(debug=True)


