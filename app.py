
# Import your Python Libraries (you may need boto3 for AWS)
import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np


# Connects Dash -> Flask (for wsgi/gunicorn production server)
app = Dash(__name__)
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.5, size=x.shape)

# Create a Plotly figure
figure = go.Figure()

figure.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(size=10, color='rgba(255, 182, 193, .9)', line=dict(width=2, color='rgba(255, 182, 193, .9)')),
    name='Random Data'
))

figure.update_layout(
    title='Random Scatter Plot',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    template='plotly_dark'
)

# needed for gunicorn/wsgi to connect
server = app.server

# Your visualization code goes here etc.
app.layout = html.Div([
    html.H1("Random Plotly Graph"),
    dcc.Graph(figure=figure)
])

if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', port=8501)

