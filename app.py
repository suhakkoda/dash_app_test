
# Import your Python Libraries (you may need boto3 for AWS)
from dash import Dash, dcc, html, Input, Output
import os

# Connects Dash -> Flask (for wsgi/gunicorn production server)
app = Dash(__name__)

# needed for gunicorn/wsgi to connect
server = app.server

# Your visualization code goes here etc.
app.layout = html.Div([
    html.H2('Hello World')
])

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', port=8501)

