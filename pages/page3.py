from dash import dcc, html, callback, Input, Output, register_page
import pandas as pd
from plots import EmploymentAnalysis

register_page(__name__, path="/page3")

df = pd.read_excel("clean/clean_uk_emp_v2.xlsx")
analysis = EmploymentAnalysis(df)


layout = html.Div([
        html.H2("part_time_employment_page"),
        html.P("Select gender to display:"),
        dcc.Dropdown(
            id='part-time-employment-dropdown',
            options=[{'label': gender, 'value': gender} for gender in ['Male','Female']],
            value=['Male','Female'],
            multi=True,
            style={"width":'50%'}
        ),
        dcc.Graph(id='part-time-employment-graph'),
    ])


@callback(Output('part-time-employment-graph', 'figure'), Input('part-time-employment-dropdown', 'value'))
def update_parttime_employment_graph(selected_genders):
    return analysis.part_time_employment(selected_genders or ['Male','Female'])





