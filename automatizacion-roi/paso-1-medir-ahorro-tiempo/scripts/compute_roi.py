#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
compute_roi.py
Script para calcular el ROI (*Return on Investment – Retorno de la Inversión*)
y KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*).
Incluye cálculo, generación de informe y guardado de resultados.
"""

import argparse
from pathlib import Path
import sys
import pandas as pd
import numpy as np


def calcular_kpis(df, coste_hora, coste_mensual_ia, currency="EUR"):
    """Calcula KPIs y ROI a partir de un DataFrame con tareas y tiempos antes/después."""
    # Validaciones mínimas
    if not {"tarea", "minutos_antes", "minutos_despues", "volumen_mensual"} <= set(df.columns):
        raise ValueError("El CSV debe contener las columnas requeridas.")

    df = df.copy()
    df["ahorro_minutos"] = df["minutos_antes"] - df["minutos_despues"]
    df["ahorro_pct"] = df["ahorro_minutos"] / df["minutos_antes"]

    df["coste_base"] = (df["minutos_antes"] * df["volumen_mensual"] * coste_hora) / 60
    df["coste_ia_operativo"] = (df["minutos_despues"] * df["volumen_mensual"] * coste_hora) / 60

    total_volumen = df["volumen_mensual"].sum()
    df["coste_ia_licencia"] = (
        (df["volumen_mensual"] / total_volumen) * coste_mensual_ia if total_volumen > 0 else 0
    )
    df["coste_ia_total"] = df["coste_ia_operativo"] + df["coste_ia_licencia"]

    df["beneficio"] = df["coste_base"] - df["coste_ia_total"]
    df["roi_pct"] = np.where(
        df["coste_ia_total"] > 0, (df["beneficio"] / df["coste_ia_total"]) * 100, np.nan
    )

    # Fila TOTAL agregada
    total = pd.DataFrame({
        "tarea": ["TOTAL"],
        "minutos_antes": [np.average(df["minutos_antes"], weights=df["volumen_mensual"])],
        "minutos_despues": [np.average(df["minutos_despues"], weights=df["volumen_mensual"])],
        "volumen_mensual": [df["volumen_mensual"].sum()],
        "ahorro_minutos": [np.average(df["ahorro_minutos"], weights=df["volumen_mensual"])],
        "ahorro_pct": [np.average(df["ahorro_pct"], weights=df["volumen_mensual"])],
        "coste_base": [df["coste_base"].sum()],
        "coste_ia_operativo": [df["coste_ia_operativo"].sum()],
        "coste_ia_licencia": [df["coste_ia_licencia"].sum()],
        "coste_ia_total": [df["coste_ia_total"].sum()],
        "beneficio": [df["beneficio"].sum()],
        "roi_pct": [
            (df["beneficio"].sum() / df["coste_ia_total"].sum() * 100)
            if df["coste_ia_total"].sum() > 0 else np.nan
        ],
        "currency": [currency],
    })

    df["currency"] = currency
    return pd.concat([df, total], ignore_index=True)


def generar_resumen_md(df):
    """Genera un informe en Markdown con los principales resultados (fila TOTAL)."""
    total = df[df["tarea"] == "TOTAL"].iloc[0]
    return f"""# Resumen ROI
- **Ahorro medio ponderado:** {total['ahorro_minutos']:.1f} min ({total['ahorro_pct']*100:.1f}%)
- **Coste base mensual:** {total['coste_base']:.2f} EUR
- **Coste IA total mensual:** {total['coste_ia_total']:.2f} EUR
- **Beneficio mensual:** {total['beneficio']:.2f} EUR
- **ROI%:** {'' if pd.isna(total['roi_pct']) else f"{total['roi_pct']:.1f}%"}
"""


def guardar_resultados(df_kpis, resumen_md, outdir: Path) -> None:
    """Guarda KPIs en CSV y resumen en Markdown en la carpeta de salida."""
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "kpis_por_tarea.csv").write_text(df_kpis.to_csv(index=False), encoding="utf-8")
    (outdir / "resumen_roi.md").write_text(resumen_md, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--hourly-rate", type=float, required=True, help="Coste por hora")
    parser.add_argument("--ai-monthly", type=float, default=0.0, help="Coste mensual IA")
    parser.add_argument("--outdir", required=True, help="Carpeta de salida")
    parser.add_argument("--currency", default="EUR", help="Moneda (defecto: EUR)")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df_kpis = calcular_kpis(df, args.hourly_rate, args.ai_monthly, args.currency)
    resumen = generar_resumen_md(df_kpis)
    guardar_resultados(df_kpis, resumen, Path(args.outdir))

    print("✅ Archivos generados en:", args.outdir)


if __name__ == "__main__":
    sys.exit(main())
