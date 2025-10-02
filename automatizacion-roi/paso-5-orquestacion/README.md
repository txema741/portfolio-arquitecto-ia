# 🚀 Paso 5 — Orquestación Avanzada

## 🎯 Objetivo
Centralizar en un **único pipeline** la ejecución de todos los pasos anteriores (1 → 4).  
Con este paso se logra:

- Automatización de todo el flujo de análisis ROI–CoPQ.
- Ejecuciones reproducibles y auditables.
- Resultados guardados en carpetas versionadas por fecha/hora.
- Posibilidad de ejecución local, programada (cron/Task Scheduler) o en CI/CD (GitHub Actions).

---

## 📂 Estructura
```bash
paso-5-orquestacion/
├── README.md
├── pipeline.py             # Script maestro que ejecuta los pasos 1–4
├── configs/
│   └── params.json         # Parámetros globales
├── logs/
│   └── ejecucion.log       # Registro histórico de ejecuciones
├── results/
│   └── run_YYYYMMDD_HHMM/  # Carpeta creada en cada ejecución
│       ├── final_report.csv
│       ├── final_report.md
│       ├── final_report.pdf
│       └── kpi_dashboard.html
└── tests/
    └── test_pipeline.py    # Verifica que el pipeline corre de inicio a fin
```
▶️ Ejecución del pipeline
Ejecución local
python paso-5-orquestacion/pipeline.py --config paso-5-orquestacion/configs/params.json

Ejemplo de params.json
{
  "hourly_rate": 25,
  "ai_monthly": 50,
  "currency": "EUR"
}

📊 Resultados esperados

Cada ejecución genera en results/run_YYYYMMDD_HHMM/:

paso1/ → resultados de ROI (compute_roi.py).

paso2/ → resultados de CoPQ (compute_copq.py).

paso3/ → resultados CLI (resumen_roi.md, kpis_por_tarea.csv, resumen_copq.md, copq_por_error.csv).

final_report.csv → Consolidado ROI + CoPQ.

final_report.md → Informe en Markdown.

final_report.pdf → Informe en PDF.

kpi_dashboard.html → Dashboard exportado.

✅ Tests automáticos

Para verificar que el pipeline corre sin errores y genera todos los outputs:

pytest paso-5-orquestacion/tests/test_pipeline.py -q


El test comprueba:

Que pipeline.py y params.json existen.

Que se crea una carpeta run_YYYYMMDD_HHMM en results/.

Que los outputs finales (final_report.*, kpi_dashboard.html) se generan.

Que los resultados intermedios de pasos 1, 2 y 3 están presentes.

📌 Conclusión

El Paso 5 convierte el proyecto en una herramienta de automatización empresarial real:
un único comando ejecuta todo el flujo y produce informes y dashboards listos para decisión.
