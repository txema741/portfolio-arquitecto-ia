#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
compute_copq.py
Calcula el CoPQ (*Cost of Poor Quality – Coste de la Mala Calidad*).
Lee un CSV con tipos de error, su frecuencia y costes, y genera métricas y resumen.
"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np

def calcular_copq(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula costes de la mala calidad por error y un total."""
    df = df.copy()
    # Coste por corrección
    df["coste_correccion"] = (df["tiempo_correccion_min"] / 60) * df["coste_hora"] * df["frec_mensual"]
    # Coste reputacional
    df["coste_reputacional"] = df["impacto_reputacional"] * df["frec_mensual"]
    # Coste total
    df["coste_total"] = df["coste_correccion"] + df["coste_reputacional"]
    # Horas perdidas
    df["horas_perdidas"] = (df["tiempo_correccion_min"] * df["frec_mensual"]) / 60

    # Fila TOTAL
    total = pd.DataFrame({
        "tipo_error": ["TOTAL"],
        "frec_mensual": [df["frec_mensual"].sum()],
        "tiempo_correccion_min": [np.average(df["tiempo_correccion_min"], weights=df["frec_mensual"])],
        "coste_hora": [np.average(df["coste_hora"], weights=df["frec_mensual"])],
        "impacto_reputacional": [np.average(df["impacto_reputacional"], weights=df["frec_mensual"])],
        "coste_correccion": [df["coste_correccion"].sum()],
        "coste_reputacional": [df["coste_reputacional"].sum()],
        "coste_total": [df["coste_total"].sum()],
        "horas_perdidas": [df["horas_perdidas"].sum()]
    })
    return pd.concat([df, total], ignore_index=True)

def generar_resumen_md(df: pd.DataFrame) -> str:
    """Genera un resumen ejecutivo en Markdown a partir del DataFrame con CoPQ."""
    total = df[df["tipo_error"] == "TOTAL"].iloc[0]
    return f"""# Resumen CoPQ
- **Coste total de la mala calidad (mensual):** {total['coste_total']:.2f} EUR
- **Coste de corrección:** {total['coste_correccion']:.2f} EUR
- **Coste reputacional:** {total['coste_reputacional']:.2f} EUR
- **Horas perdidas al mes:** {total['horas_perdidas']:.1f} h
"""

def guardar_resultados(df: pd.DataFrame, resumen_md: str, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "copq_por_error.csv").write_text(df.to_csv(index=False), encoding="utf-8")
    (outdir / "resumen_copq.md").write_text(resumen_md, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Cálculo del Coste de la Mala Calidad (CoPQ)")
    parser.add_argument("--input", required=True, help="CSV con errores y sus costes")
    parser.add_argument("--outdir", required=True, help="Carpeta de salida")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df_result = calcular_copq(df)
    resumen = generar_resumen_md(df_result)
    guardar_resultados(df_result, resumen, Path(args.outdir))

    print("✅ Archivos generados en:", args.outdir)

if __name__ == "__main__":
    main()
