from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash import page_container
import dash_bootstrap_components as dbc 

# app
app = Dash(__name__, use_pages=True,pages_folder='../pages' ,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        
        # Dropdown
        
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Employment/Sector", href="/page1"),
                dbc.DropdownMenuItem("Gender Unemployment Gap", href="/page2"),
                dbc.DropdownMenuItem("Part-Time Employment/Gender", href="/page3"),
                # Add more dashboards here as needed
            ],
            nav=True,
            in_navbar=True,
            label="Dashboards",  # Label for the dropdown
            right=True
        ),
        
        
    ],
    brand="Multi-Page Dashboard",
    brand_href="/",
    color="dark",
    dark=True,
)

# App layout
app.layout = dbc.Container(
    [
        navbar,
        dcc.Location(id='url', refresh=False),
        page_container
    ],
    fluid=True
)



if __name__ == '__main__':
    app.run_server(debug=True)






