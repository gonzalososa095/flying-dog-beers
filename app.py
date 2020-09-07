import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('https://github.com/gonzalososa095/flying-dog-beers/blob/master/data.csv',engine='python')

external_stylesheets = ['https://codepen.io/qpi65/pen/LYNOXJO.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server


def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Gonzalo Sosa"),
                    html.H6("Sound Engineer"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="contacto", children="Contacto", n_clicks=0
                    ),
                    html.Img(id="logo", src=app.get_asset_url("dash-logo-new.png")),
                ],
            ),
        ],
    )

app.layout = html.Div([
    build_banner(),
    html.H1("Directividad parlante B&D 6MD38", style={'text-align': 'center'}),

    daq.Gauge(
        id='knob',
        label="Angulo de incidencia",
        color="#42ADDC",
             value = 0,
             min = -135,
             max= 135,
             scale={'start':-135,'labelInterval':45,'interval':1},
            theme = 'Light',
    showCurrentValue = True),
    dcc.Slider(
        id='slider',
        min=-90,
        max=90,
        step=10,
        value=0),
    html.Br(),

    dcc.Graph(id='rta', figure={})

])

@app.callback([
    Output('knob', 'value'),
    Output('rta','figure')],
    [Input('slider', 'value')]
)
def update_output(value):

    dff = df.copy()

    fig = px.line(dff, x="Frecuencia", y=str(value),log_x=True,labels={str(value):'Amplitud',"Frecuencia":'Frecuencia [Hz]'},template = 'plotly_dark')
    #template = 'plotly_dark'
    return value,fig


if __name__ == '__main__':
    app.run_server()
