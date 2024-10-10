from dash import dcc, html, callback, Input, Output, register_page
import pandas as pd
from plots import EmploymentAnalysis

register_page(__name__, path="/page1")

df = pd.read_excel("clean/clean_uk_emp_v2.xlsx")
analysis = EmploymentAnalysis(df)


layout = html.Div([
        html.H2("Employment by Sector Over Time"),
        html.P("Select sectors to display:"),
        dcc.Dropdown(
            id='sector-dropdown',
            options=[{'label': sector, 'value': sector} for sector in analysis.sector_data.columns],
            value=['Agriculture', 'Industry', 'Services'],
            multi=True,
            style={"width":'50%'}
        ),
        dcc.Graph(id='employment-sector-graph'),
        
    ])

@callback(Output('employment-sector-graph', 'figure'), Input('sector-dropdown', 'value'))
def update_employment_graph(selected_sectors):
    return analysis.employment_by_sector(selected_sectors or ['Agriculture', 'Industry', 'Services'])




