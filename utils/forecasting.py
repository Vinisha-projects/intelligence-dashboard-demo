
from prophet import Prophet
import pandas as pd
import plotly.graph_objs as go

def plot_forecast(df):
    df = df.rename(columns={df.columns[0]: 'ds', df.columns[1]: 'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast'))
    return fig
