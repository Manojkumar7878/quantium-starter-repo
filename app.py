import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Print all region values
print(df["region"].unique())

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "margin": "20px"}
    ),

    dcc.Graph(id="sales-chart")
])

# Callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    # Group by date
    sales = filtered_df.groupby("date", as_index=False)["sales"].sum()

    # Create line chart
    fig = px.line(
        sales,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)