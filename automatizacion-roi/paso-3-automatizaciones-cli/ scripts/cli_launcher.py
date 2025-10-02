#!/usr/bin/env python3
"""
CLI Launcher para automatizar ROI y CoPQ.
Permite elegir desde terminal qué cálculo ejecutar.
"""

import argparse
import subprocess
import sys

def run_roi(args):
    cmd = [
        "python", "automatizacionRoi/paso-1-medir-ahorro-tiempo/scripts/compute_roi.py",
        "--input", args.input,
        "--hourly-rate", str(args.hourly_rate),
        "--ai-monthly", str(args.ai_monthly),
        "--outdir", args.outdir,
        "--currency", args.currency
    ]
    subprocess.run(cmd, check=True)

def run_copq(args):
    cmd = [
        "python", "automatizacionRoi/paso-2-medir-calidad-errores/scripts/compute_copq.py",
        "--input", args.input,
        "--outdir", args.outdir
    ]
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(
        description="CLI Launcher para ROI y CoPQ"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando ROI
    roi_parser = subparsers.add_parser("roi", help="Ejecutar cálculo ROI")
    roi_parser.add_argument("--input", required=True, help="Ruta al CSV de tareas")
    roi_parser.add_argument("--hourly-rate", required=True, type=float, help="Coste por hora (€)")
    roi_parser.add_argument("--ai-monthly", required=True, type=float, help="Coste mensual IA (€)")
    roi_parser.add_argument("--outdir", required=True, help="Carpeta de resultados")
    roi_parser.add_argument("--currency", default="EUR", help="Moneda (EUR/USD)")

    # Subcomando CoPQ
    copq_parser = subparsers.add_parser("copq", help="Ejecutar cálculo CoPQ")
    copq_parser.add_argument("--input", required=True, help="Ruta al CSV de errores")
    copq_parser.add_argument("--outdir", required=True, help="Carpeta de resultados")

    args = parser.parse_args()

    if args.command == "roi":
        run_roi(args)
    elif args.command == "copq":
        run_copq(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
