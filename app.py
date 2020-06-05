# -*- coding: utf-8 -*-

import dash

import layout


external_scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML",  # MathJax for TeX
]
external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css"  # default Dash stylesheet
]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)

app.title = "Interpretable Machine Learning"
app.layout = layout.get_app_layout()

if __name__ == "__main__":
    app.run_server(
        host="0.0.0.0",
        debug=True,
    )
