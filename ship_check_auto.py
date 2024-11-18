##################################################
#Automation of Ship Check
#11/17/2024
#Efrain Alvarez
##################################################

import pandas as pd
from dash import Dash, dcc, html

app = Dash()

app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(debug=True)
