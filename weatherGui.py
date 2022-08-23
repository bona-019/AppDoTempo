import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from weatherStyles import Styles
from weatherRequest import Weather as wr

ws = Styles()

dropdownMenu = [
    dbc.DropdownMenu(label='Cidade', color='info', size='lg', children=[
        dbc.DropdownMenuItem('Campinas', id='cidade-cps'),
        dbc.DropdownMenuItem('São Paulo', id='cidade-sp'),
        dbc.DropdownMenuItem('Rio de Janeiro', id='cidade-rj'),
        dbc.DropdownMenuItem('Fortaleza', id='cidade-frt'),], style=ws.dropdownMenu(), direction='end', id='dropdownmenu')]

tempText = [
    dbc.Col([html.H3('Temperatura', style=ws.tempText())], md=3),
    dbc.Col([html.H3('Sensação', style=ws.tempText())], md=3),
    dbc.Col([html.H3('Mínima', style=ws.tempText())], md=3),
    dbc.Col([html.H3('Máxima', style=ws.tempText())], md=3)]

tempValues = [
    dbc.Col([html.H3('', id='temp-output', style=ws.tempValues()['temp'])], md=3),
    dbc.Col([html.H3('', id='sense-output', style=ws.tempValues()['sense'])], md=3),
    dbc.Col([html.H3('', id='min-output', style=ws.tempValues()['min'])], md=3),
    dbc.Col([html.H3('', id='max-output', style=ws.tempValues()['max'])], md=3)
]

header = [
    html.H1("App do Tempo", style=ws.showHeader()),
    html.H3("", id='cidade-output', style=ws.showCidade()),
    dcc.Loading(
        html.P("", id='desc-output', style=ws.showDesc())),
    dbc.Row(tempText),
    dcc.Loading(
        dbc.Row(tempValues), type='circle')]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.Div(dropdownMenu)            
        ], md=3),

        dbc.Col([html.Div(header)], md=6)
        
    ]) # Row
]) # container

@app.callback(
    Output('cidade-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_cidade(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return id_lookup[button_id]

@app.callback(
    Output('desc-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_desc(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return wr(id_lookup[button_id], 'metric', 'pt_br').showDesc()

@app.callback(
    Output('temp-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_temp(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return wr(id_lookup[button_id], 'metric', 'pt_br').showTemp()

@app.callback(
    Output('sense-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_sense(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return wr(id_lookup[button_id], 'metric', 'pt_br').showSense()

@app.callback(
    Output('min-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_min(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return wr(id_lookup[button_id], 'metric', 'pt_br').showTempMin()

@app.callback(
    Output('max-output', 'children'),
    Input('cidade-cps', 'n_clicks'),
    Input('cidade-sp', 'n_clicks'),
    Input('cidade-rj', 'n_clicks'),
    Input('cidade-frt', 'n_clicks'),
)

def display_max(n1, n2, n3, n4):
    id_lookup = {'cidade-cps': 'Campinas', 'cidade-sp': 'São Paulo', 'cidade-rj': 'Rio de Janeiro', 'cidade-frt': 'Fortaleza'}
    ctx = dash.callback_context

    if (n1 is None and n2 is None and n3 is None and n4 is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]['prop_id'].split(".")[0]
    return wr(id_lookup[button_id], 'metric', 'pt_br').showTempMax()

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
    