import pandas as pd
from ..scripts import charts

def test_charts_functions():
    df = pd.DataFrame({
        "ROI": [0.2, 0.3],
        "Payback": [12, 14],
        "Tipo_Error": ["Crítico", "Mayor"],
        "CoPQ_Estimado(EUR)": [5000, 2000]
    })

    fig1 = charts.plot_roi(df)
    fig2 = charts.plot_payback(df)
    fig3 = charts.plot_copq(df)

    assert fig1 is not None
    assert fig2 is not None
    assert fig3 is not None
