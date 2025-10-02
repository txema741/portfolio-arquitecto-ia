# -*- coding: utf-8 -*-
"""
Test unitario básico para compute_copq.py
"""

import pandas as pd
from pathlib import Path
import tempfile
import sys

CURRENT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = (CURRENT_DIR / ".." / "scripts").resolve()
sys.path.insert(0, str(SCRIPTS_DIR))

from compute_copq import calcular_copq, generar_resumen_md, guardar_resultados  # noqa: E402

def test_copq_basico():
    df = pd.DataFrame({
        "tipo_error": ["A", "B"],
        "frec_mensual": [10, 5],
        "tiempo_correccion_min": [10, 20],
        "coste_hora": [25, 30],
        "impacto_reputacional": [50, 100]
    })

    result = calcular_copq(df)
    assert "TOTAL" in result["tipo_error"].values

    resumen = generar_resumen_md(result)
    assert "Coste total" in resumen

    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td)
        guardar_resultados(result, resumen, outdir)
        assert (outdir / "copq_por_error.csv").exists()
        assert (outdir / "resumen_copq.md").exists()
