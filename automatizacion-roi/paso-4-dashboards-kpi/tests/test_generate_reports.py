import os
import pandas as pd
import subprocess

def test_generate_reports(tmp_path):
    # Crear CSVs de prueba
    roi_file = tmp_path / "kpis_por_tarea.csv"
    copq_file = tmp_path / "copq_por_error.csv"

    pd.DataFrame({
        "Tarea": ["A", "B"],
        "ROI": [0.2, 0.3],
        "Payback": [12, 14]
    }).to_csv(roi_file, index=False)

    pd.DataFrame({
        "Tipo_Error": ["Crítico", "Mayor"],
        "CoPQ_Estimado(EUR)": [5000, 2000]
    }).to_csv(copq_file, index=False)

    outdir = tmp_path
    cmd = [
        "python", "automatizacionRoi/paso-4-dashboards-kpi/scripts/generate_reports.py",
        "--roi", str(roi_file),
        "--copq", str(copq_file),
        "--outdir", str(outdir)
    ]

    result = subprocess.run(cmd, capture_output=True)
    assert result.returncode == 0
    assert (outdir / "final_report.csv").exists()
    assert (outdir / "final_report.md").exists()
