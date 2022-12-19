from jupyter_dash import JupyterDash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd

poverty_data = pd.read_csv('data/PovStatsData.csv')
country_data = pd.read_csv('data/PovStatsData.csv')

# , external_stylesheets=[dbc.themes.BOOTSTRAP]
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Dropdown(id='country', options=[{'label': country, 'value': country}
                                        for country in
                                        poverty_data['Country Name'].unique()
                                        ]),
    html.Div(id='report'),

    html.H1('Poverty and Equity Database',
            style={'color': 'blue',
                   'fontSize': '40px'}),
    html.H2('The World Bank'),
    dbc.Tabs([
        dbc.Tab([
            html.P('Key Facts'),
            html.Ul([
                html.Li('Number of Economies: 170'),
                html.Li('Temporal Coverage: 1974 - 2019'),
                html.Li('Update Frequency: Quarterly'),
                html.Li('Last Updated: March 18, 2020'),
                html.Li(['Source: ',
                         html.A('https://datacatalog.worldbank.org/dataset/'
                                'poverty-and-equity-database',
                                href='https://datacatalog.worldbank.org/'
                                     'dataset/poverty-and-equity-database'),
                         ])

            ])
        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps '
                        'with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                         html.A(
                             'https://github.com/PacktPublishing/Interactive-'
                             'Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                             href='https://github.com/PacktPublishing/'
                                  'Interactive-Dashboards-and-Data-Apps-with'
                                  '-Plotly-and-Dash')]),

            ])
        ], label='Project Info')
    ])

])


@app.callback(Output('report', 'children'),
              Input('country', 'value'))
def display_country_report(country):
    if country is None:
        return ''
    filtered_df = country_data[(country_data['Country Name'] == country)
                               & (country_data[
                                      'Indicator Name'] == 'Population, '
                                                           'total')]
    population = filtered_df.loc[:, '2010'].values[0]
    return [html.H3(country),
            'The population of %s in 2010 was %d.' % (country, population)]
