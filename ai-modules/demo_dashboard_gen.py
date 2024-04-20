import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_csv('vgsales.csv')
print(df)
# Example: Calculate average sales
average_sales = df['EU_Sales'].mean()



# Example: Create a bar chart for sales by month
fig = go.Figure()
fig.add_trace(go.Bar(x=df['Year'], y=df['EU_Sales']))
fig.update_layout(title='Sales by Year', xaxis_title='Year', yaxis_title='EU_Sales')
fig.show()



app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Your Dashboard'),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    # Add more components as needed
])

if __name__ == '__main__':
    app.run_server(debug=True)