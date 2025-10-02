# Automatización + ROI Empresarial

## Objetivo
Medir y demostrar **ROI (Return on Investment – Retorno de la Inversión)** de casos IA con scripts reproducibles, datasets sintéticos y pruebas.

## Estructura
- `/scripts/` → `calc_roi.py`, `simulate_costs.py`, `tests/`
- `/data_sample/` → CSV/XLSX sintéticos
- `/results/` → reportes MD/PDF, gráficos
- `/docs/` → metodología, supuestos

## Fórmulas base
ROI = (Beneficio − Coste) / Coste  
Payback (meses), NPV, *sensitivity ±20%*

## KPI
- **KPI**: ahorro horas/mes, reducción errores, *latency* p95, adopción.

## Cómo ejecutar
```bash
python scripts/calc_roi.py --input data_sample/caso.csv --outdir results --pdf
pytest -q
