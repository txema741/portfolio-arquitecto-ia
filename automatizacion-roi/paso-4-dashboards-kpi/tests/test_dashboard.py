import os
import pandas as pd
from ..scripts import dashboard

def test_load_data(tmp_path):
    csv_file = tmp_path / "final_report.csv"
    pd.DataFrame({
        "ROI": [0.2, 0.3],
        "Payback": [12, 14]
    }).to_csv(csv_file, index=False)

    df = dashboard.load_data(csv_file)
    assert not df.empty
    assert "ROI" in df.columns
