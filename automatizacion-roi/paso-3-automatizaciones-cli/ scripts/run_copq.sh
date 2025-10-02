#!/bin/bash
# Script para automatizar la ejecución del cálculo CoPQ
# ⚠️ Asegúrate de dar permisos con: chmod +x run_copq.sh

python automatizacionRoi/paso-2-medir-calidad-errores/scripts/compute_copq.py \
  --input automatizacionRoi/paso-2-medir-calidad-errores/data_sample/errores_dataset.csv \
  --outdir automatizacionRoi/paso-2-medir-calidad-errores/results
