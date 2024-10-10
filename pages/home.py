from dash import html, dcc, register_page

register_page(__name__, path="/")

layout = html.Div([
    html.H1("Welcome to the Home Page"),
    html.P("This is the landing page of your multi-page Dash app."),

    # Section for List of Dashboards
    html.H1("List of Dashboards"),
    
    html.Div([
        html.H3("Employment by Sector Over Time"),
        html.P("This Dashboard showcases employment trends across various sectors over a defined time period, showing shifts in workforce distribution across industries."),
        dcc.Link('Go to Employment by Sector Dashboard', href='/page1'),
    ], style={"marginBottom": "30px"}),

    html.Div([
        html.H3("Gender Unemployment Gap"),
        html.P("This Dashboard illustrates the difference in unemployment rates between men and women, highlighting the gender disparity in unemployment over time."),
        dcc.Link('Go to Gender Unemployment Dashboard', href='/page2'),
    ], style={"marginBottom": "30px"}),
    
    html.Div([
        html.H3("Part-Time Employment by Gender"),
        html.P("This Dashboard showcases the proportion of part-time workers between men and women, indicating trends in part-time employment distribution by gender."),
        dcc.Link('Go to Customer Insights Dashboard', href='/page3'),
    ], style={"marginBottom": "30px"})
    
    
])
