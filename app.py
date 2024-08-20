Less minimal app.py code here:
https://dash.plotly.com/deployment
+ 
correct invocation line here:
https://community.plotly.com/t/error-with-gunicorn-application-object-must-be-callable/31397 

test invoke with: (but will end when your ec2 terminal session ends, resets, etc.)
    $ gunicorn app:server --bind=0.0.0.0:8501

For persistent production you will need: (end with kill process number) 
    (ENV)$ nohup gunicorn app:server --bind=0.0.0.0:8501 &
    or
    (ENV)$ screen gunicorn app:server --bind=0.0.0.0:8501 &


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

