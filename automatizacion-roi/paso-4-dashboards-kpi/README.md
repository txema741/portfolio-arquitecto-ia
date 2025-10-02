📂 Paso 4 — Reporting y Dashboards KPI
🎯 Objetivo

Transformar los resultados del Paso 3 (resumen_roi.md, kpis_por_tarea.csv, resumen_copq.md, copq_por_error.csv) en:

Informes finales (final_report.csv, final_report.md, final_report.pdf).

Dashboards interactivos (Streamlit/Plotly).

Proveer tanto reportes estáticos para directivos como dashboards dinámicos para analistas.

📦 Estructura de carpetas
automatizacionRoi/
└── paso-4-dashboards-kpi/
    ├── README.md
    ├── scripts/
    │   ├── generate_reports.py     # Genera informes en CSV, MD y PDF
    │   ├── dashboard.py            # Dashboard interactivo (Streamlit/Plotly)
    │   ├── charts.py               # Funciones de gráficos
    │   └── __init__.py
    │
    ├── results/
    │   ├── final_report.csv        # Reporte consolidado de KPIs
    │   ├── final_report.md         # Informe en Markdown
    │   ├── final_report.pdf        # Informe en PDF
    │   └── kpi_dashboard.html      # Dashboard exportado como HTML
    │
    ├── tests/
    │   ├── test_generate_reports.py
    │   ├── test_dashboard.py
    │   └── test_charts.py
    │
    └── requirements.txt            # Dependencias: streamlit, plotly, pandas, matplotlib, reportlab

📥 Datos de entrada

paso-3-automatizaciones-cli/results/resumen_roi.md

paso-3-automatizaciones-cli/results/kpis_por_tarea.csv

paso-3-automatizaciones-cli/results/resumen_copq.md

paso-3-automatizaciones-cli/results/copq_por_error.csv

▶️ Ejecución
Generación de reportes
python paso-4-dashboards-kpi/scripts/generate_reports.py \
  --roi paso-3-automatizaciones-cli/results/kpis_por_tarea.csv \
  --copq paso-3-automatizaciones-cli/results/copq_por_error.csv \
  --outdir paso-4-dashboards-kpi/results/ \
  --pdf


👉 Produce:

final_report.csv

final_report.md

final_report.pdf

Dashboard interactivo
streamlit run paso-4-dashboards-kpi/scripts/dashboard.py


👉 Permite filtrar por escenarios, ver gráficas dinámicas y KPIs con semáforos.

Exportación estática
python paso-4-dashboards-kpi/scripts/dashboard.py \
  --input paso-4-dashboards-kpi/results/final_report.csv \
  --export paso-4-dashboards-kpi/results/kpi_dashboard.html


👉 Produce:

kpi_dashboard.html

📊 Resultados esperados

Informes corporativos (final_report.*) para ejecutivos.

Dashboard KPI interactivo para analistas y equipos.

KPIs visuales con semáforos:

Verde ≥ 20%

Amarillo 10–20%

Rojo < 10%

✅ Control de calidad

Verificar que los CSV de Paso 3 no tengan NaN.

Revisar que los reportes se generan en los tres formatos.

Confirmar que el dashboard carga sin errores y exporta a HTML.

📌 Conclusión

El Paso 4 convierte las automatizaciones CLI en informes y dashboards listos para cliente, uniendo rigor técnico y presentación visual.
Con esto, el flujo ROI–CoPQ queda cerrado: datos → cálculos → reporting → visualización.
