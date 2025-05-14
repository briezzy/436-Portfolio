from Vis.finalAss1 import make_finalAss1
from Vis.misleadingVis import make_misleadingVis
import dash
from dash import dcc, html
import os

DATASETS_PATH = os.path.join("Vis", "datasets")

def initialize_dashboard(datasets_path):
    # Initialize the Dash app
    app = dash.Dash(__name__)

    app.layout = html.Div([
    html.H1("Individual portfolio", style={'textAlign': 'center'}),

    # Summary Section
    html.Div([
        html.P("""This dashboard visualizes insights into media trends using various visual artifacts. 
            It includes a bubble chart and a deliberately misleading chart to demonstrate the importance 
            of ethical data visualization. Users can observe how visualization techniques affect interpretation.""",
    ], style={
        'padding': '20px',
        'backgroundColor': '#f9f9f9',
        'borderBottom': '1px solid #ccc',
        'fontSize': '16px',
        'lineHeight': '1.6'
    }),

        html.Div([
            dcc.Graph(figure=make_finalAss1(datasets_path)),
            dcc.Graph(figure=make_misleadingVis(datasets_path)),
            html.Img(src='/assets/finalass1.png', style={'width': '100%', 'marginBottom': '40px'}),
            html.Img(src='/assets/misleadingVis.png', style={'width': '100%'})
        ], style={
            'display': 'block',
            'padding': '20px'
        })
    ])

    return app

if __name__ == "__main__":
    app = initialize_dashboard(DATASETS_PATH)
    app.run(debug=True)
