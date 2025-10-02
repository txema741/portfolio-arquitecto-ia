# -*- coding: utf-8 -*-
"""
Test unitario para compute_roi.py

Valida:
1. Cálculo de KPIs con dataset de ejemplo.
2. Presencia de fila TOTAL.
3. ROI% válido cuando coste_ia_total > 0.
4. Resumen Markdown con información clave.
5. Guardado de resultados en disco.
"""

import pandas as pd
from pathlib import Path
import tempfile
import sys

# Añadimos la carpeta scripts al sys.path
CURRENT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = (CURRENT_DIR / ".." / "scripts").resolve()
sys.path.insert(0, str(SCRIPTS_DIR))

from compute_roi import calcular_kpis, generar_resumen_md, guardar_resultados  # noqa: E402


def test_calculo_roi_basico():
    # Dataset mínimo
    df = pd.DataFrame({
        "tarea": ["A", "B"],
        "minutos_antes": [40, 30],
        "minutos_despues": [20, 15],
        "volumen_mensual": [10, 20],
    })

    coste_hora = 25.0
    coste_mensual_ia = 50.0
    currency = "EUR"

    # Cálculo
    kpis = calcular_kpis(df, coste_hora, coste_mensual_ia, currency)

    # Debe existir la fila TOTAL
    assert "TOTAL" in set(kpis["tarea"].tolist()), "Falta fila TOTAL."

    # ROI% debe ser válido cuando hay coste_ia_total > 0
    total = kpis[kpis["tarea"] == "TOTAL"].iloc[0]
    assert total["coste_ia_total"] > 0
    assert pd.notna(total["roi_pct"]), "ROI% no debería ser NaN."

    # Resumen Markdown debe contener campos clave
    resumen = generar_resumen_md(kpis)
    assert "Resumen ROI" in resumen
    assert "Beneficio mensual" in resumen
    assert currency in resumen

    # Guardado de resultados
    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "results"
        guardar_resultados(kpis, resumen, outdir)
        assert (outdir / "kpis_por_tarea.csv").exists()
        assert (outdir / "resumen_roi.md").exists()
