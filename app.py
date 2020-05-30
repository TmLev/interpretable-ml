# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html


external_scripts = ["https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML"]
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)

app.layout = html.Div(
    children=[
        html.Div(children="$$x = 1$$"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
