# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash('Gráfico')

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [4, 1, 2, 2, 4, 3 ],
    "Cidades": ["Maluco", "Maluco", "Maluco", "Ceará", "Ceará", "Ceará"]
})
fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidades", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Teste de gráficos'),
    html.H2(children='Título 2'),
    html.Div(children='''
        Gráfico criado com Dash.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)