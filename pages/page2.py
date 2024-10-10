from dash import dcc, html, callback, Input, Output, register_page
import pandas as pd
from plots import EmploymentAnalysis

register_page(__name__, path="/page2")

df = pd.read_excel("clean/clean_uk_emp_v2.xlsx")
analysis = EmploymentAnalysis(df)


layout = html.Div([
        html.H2("Gender Unemployment Gap Page"),
        html.P("Select gender to display:"),
        dcc.Dropdown(
            id='gender-unemployment-dropdown',
            options=[{'label': gender, 'value': gender} for gender in ['Male','Female']],
            value=['Male','Female'],
            multi=True,
            style={"width":'50%'}
        ),
        dcc.Graph(id='gender-unemployment-graph'),
    ])


@callback(Output('gender-unemployment-graph', 'figure'), Input('gender-unemployment-dropdown', 'value'))
def update_gender_unemployment_graph(selected_genders):
    return analysis.gender_unemployment_gap(selected_genders or ['Male','Female'])

