import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def plotly_scatters_double_y_axis(df, x, y, y2):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    x_data = x
    y_data = y
    y2_data = y2
    if df is not None:
        if isinstance(x, str) and x in df.columns:
            x_data = df[x]
        elif isinstance(x, pd.Series):
            x_data = x.tolist()

        if isinstance(y, str) and y in df.columns:
            y_data = df[y]
        elif isinstance(y, pd.Series):
            y_data = y.tolist()

        if isinstance(y2, str) and y2 in df.columns:
            y2_data = df[y2]
        elif isinstance(y2, pd.Series):
            y2_data = y2.tolist()
    # Add traces
    fig.add_trace(
        go.Scatter(x=x_data, y=y_data, name="yaxis data"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=x_data, y=y2_data, name="yaxis2 data"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(title_text="Double Y Axis Example")

    # Set x-axis title
    fig.update_xaxes(title_text="xaxis title")

    # Set y-axes titles
    fig.update_yaxes(title_text="primary yaxis title", secondary_y=False)
    fig.update_yaxes(title_text="secondary yaxis title", secondary_y=True)

    fig.update_yaxes(
        rangemode="tozero",
        scaleanchor="y",
        scaleratio=1,
        constraintoward="bottom",
        secondary_y=True,
    )
    fig.update_yaxes(
        rangemode="tozero",
        scaleanchor="y2",
        scaleratio=1,
        constraintoward="bottom",
        secondary_y=False,
    )
    fig.show()


def plotly_bars_double_y_axis(df, x, y, y2):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    x_data = x
    y_data = y
    y2_data = y2
    if df is not None:
        if isinstance(x, str) and x in df.columns:
            x_data = df[x]
        elif isinstance(x, pd.Series):
            x_data = x.tolist()

        if isinstance(y, str) and y in df.columns:
            y_data = df[y]
        elif isinstance(y, pd.Series):
            y_data = y.tolist()

        if isinstance(y2, str) and y2 in df.columns:
            y2_data = df[y2]
        elif isinstance(y2, pd.Series):
            y2_data = y2.tolist()
    # Add traces
    fig.add_trace(
        go.Bar(x=x_data, y=y_data, name="yaxis data"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Bar(x=x_data, y=y2_data, name="yaxis2 data"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(title_text="Double Y Axis Example")

    # Set x-axis title
    fig.update_xaxes(title_text="xaxis title")

    # Set y-axes titles
    fig.update_yaxes(title_text="primary yaxis title", secondary_y=False)
    fig.update_yaxes(title_text="secondary yaxis title", secondary_y=True)

    fig.update_yaxes(
        rangemode="tozero",
        scaleanchor="y",
        scaleratio=1,
        constraintoward="bottom",
        secondary_y=True,
    )
    fig.update_yaxes(
        rangemode="tozero",
        scaleanchor="y2",
        scaleratio=1,
        constraintoward="bottom",
        secondary_y=False,
    )
    fig.show()


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "x": ["group_A", "group_B", "group_C", "group_D"],
            "y": [10, 80, 100, 250],
            "y2": [20, 50, 80, 150],
            "z": ["type1", "type2", "type2", "type1"],
        }
    )
    # scatter plots with double y-axis
    # type1: columns of the dataframe
    # plotly_scatters_double_y_axis(df, "x", "y", "y2")
    # type2: pd.Series
    # plotly_scatters_double_y_axis(None, df["x"], df["y"], df["y2"])
    # type3: lists
    # x = ["group_A", "group_B", "group_C", "group_D"]
    # y = [10, 80, 100, 250]
    # y2 = [20, 50, 80, 150]
    # plotly_scatters_double_y_axis(None, x, y, y2)

    # bar plots with double y-axis
    plotly_bars_double_y_axis(df, "x", "y", "y2")
