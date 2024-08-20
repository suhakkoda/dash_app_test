
# Import your Python Libraries (you may need boto3 for AWS)
from dash import Dash, dcc, html, Input, Output ####
import plotly.graph_objs as go
import numpy as np

# Connects Dash -> Flask (for wsgi/gunicorn production server)
app = Dash(__name__) ####

# needed for gunicorn/wsgi to connect
server = app.server ####

# Generate random data
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)
y4 = np.cos(x) + np.random.normal(0, 0.1, size=x.shape)

# Define layout with dropdowns and graphs
app.layout = html.Div([
    html.H1("Interactive Dash App with Multiple Graphs"),

    # Dropdowns for selecting data
    html.Div([
        html.Label("Select Data for Scatter Plot:"),
        dcc.Dropdown(
            id='scatter-dropdown',
            options=[
                {'label': 'Sine Wave', 'value': 'sine'},
                {'label': 'Noisy Sine Wave', 'value': 'noisy_sine'}
            ],
            value='sine'
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Select Data for Line Plot:"),
        dcc.Dropdown(
            id='line-dropdown',
            options=[
                {'label': 'Cosine Wave', 'value': 'cosine'},
                {'label': 'Noisy Cosine Wave', 'value': 'noisy_cosine'}
            ],
            value='cosine'
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    # Graphs
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='line-plot')
])

# Callbacks to update graphs based on dropdown selections
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-dropdown', 'value')]
)
def update_scatter_plot(selected_data):
    if selected_data == 'sine':
        y_data = y1
        title = 'Scatter Plot of Sine Wave'
    else:
        y_data = y3
        title = 'Scatter Plot of Noisy Sine Wave'

    return {
        'data': [go.Scatter(x=x, y=y_data, mode='markers')],
        'layout': go.Layout(title=title, xaxis={'title': 'X Axis'}, yaxis={'title': 'Y Axis'})
    }

@app.callback(
    Output('line-plot', 'figure'),
    [Input('line-dropdown', 'value')]
)
def update_line_plot(selected_data):
    if selected_data == 'cosine':
        y_data = y2
        title = 'Line Plot of Cosine Wave'
    else:
        y_data = y4
        title = 'Line Plot of Noisy Cosine Wave'

    return {
        'data': [go.Scatter(x=x, y=y_data, mode='lines')],
        'layout': go.Layout(title=title, xaxis={'title': 'X Axis'}, yaxis={'title': 'Y Axis'})
    }

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8501) ####


