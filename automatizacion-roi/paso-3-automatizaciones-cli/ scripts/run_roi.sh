#!/bin/bash
# Script para automatizar la ejecución del cálculo ROI
# ⚠️ Asegúrate de dar permisos con: chmod +x run_roi.sh

python automatizacionRoi/paso-1-medir-ahorro-tiempo/scripts/compute_roi.py \
  --input automatizacionRoi/paso-1-medir-ahorro-tiempo/data_sample/tareas_antes_despues.csv \
  --hourly-rate 25 \
  --ai-monthly 50 \
  --outdir automatizacionRoi/paso-1-medir-ahorro-tiempo/results \
  --currency EUR
