
from sklearn.ensemble import IsolationForest
import plotly.graph_objs as go

def plot_anomalies(df):
    clf = IsolationForest(contamination=0.1)
    df['anomaly'] = clf.fit_predict(df[[df.columns[1]]])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[df.columns[0]], y=df[df.columns[1]], mode='lines', name='Data'))
    anomalies = df[df['anomaly'] == -1]
    fig.add_trace(go.Scatter(x=anomalies[df.columns[0]], y=anomalies[df.columns[1]], mode='markers', name='Anomalies'))
    return fig
