import plotly.express as px

def plot_roi(df):
    return px.bar(df, x=df.index, y="ROI", title="Evolución del ROI")

def plot_payback(df):
    return px.line(df, x=df.index, y="Payback", title="Payback en meses")

def plot_copq(df):
    return px.pie(df, names="Tipo_Error", values="CoPQ_Estimado(EUR)", title="Distribución de CoPQ")
