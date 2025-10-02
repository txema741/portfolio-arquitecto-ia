# Paso 1 — Medir Ahorro de Tiempo → ROI (*Return on Investment – Retorno de la Inversión*) mínimo viable

Este paso convierte minutos ahorrados por tarea en **ROI** y **KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*)** auditables. Es el **MVP (*Minimum Viable Product – Producto Mínimo Viable*)** para demostrar impacto económico antes de escalar.

---

## 📦 Estructura del paso
```plaintext
paso-1-medir-ahorro-tiempo/
├── README.md                      # Este archivo
├── requirements.txt               # Dependencias (pandas, numpy)
├── data_sample/
│   └── tareas_antes_despues.csv   # Datos de ejemplo
├── scripts/
│   └── compute_roi.py             # Script de cálculo
├── results/
│   └── (kpis_por_tarea.csv, resumen_roi.md)
└── tests/
    └── test_compute_roi.py        # Tests mínimos (opcional)

📥 Datos de entrada

Archivo CSV de ejemplo (data_sample/tareas_antes_despues.csv):

tarea,minutos_antes,minutos_despues,volumen_mensual
Redacción de informe mensual,45,20,10
Limpieza de datos,30,12,20
Preparación de presentación,60,40,6
Revisión de contratos,35,28,15


Esquema requerido:

tarea → nombre de la actividad

minutos_antes → duración promedio antes de IA

minutos_despues → duración promedio después de IA

volumen_mensual → frecuencia de la tarea al mes

🧮 Parámetros y fórmulas

Parámetros CLI del script compute_roi.py:

--input → ruta al CSV (ej: data_sample/tareas_antes_despues.csv)

--hourly-rate → coste/hora del equipo (€/h)

--ai-monthly → coste mensual de la solución IA (licencia/inferencia), € (si no aplica, 0)

--outdir → carpeta de salida (ej: results)

--currency → moneda (defecto: EUR)

Fórmulas por tarea (mensual):

ahorro_minutos = minutos_antes − minutos_despues

ahorro_% = ahorro_minutos / minutos_antes

coste_base = (minutos_antes × volumen_mensual × hourly_rate) / 60

coste_ia_operativo = (minutos_despues × volumen_mensual × hourly_rate) / 60

coste_ia_licencia = reparto_proporcional(ai_monthly, volumen_mensual)

coste_ia_total = coste_ia_operativo + coste_ia_licencia

beneficio = coste_base − coste_ia_total

ROI_% = (beneficio / coste_ia_total) × 100 (si coste_ia_total > 0)

▶️ Cómo ejecutar
# Instalar dependencias
pip install -r paso-1-medir-ahorro-tiempo/requirements.txt

# Ejecutar cálculo
python paso-1-medir-ahorro-tiempo/scripts/compute_roi.py \
  --input paso-1-medir-ahorro-tiempo/data_sample/tareas_antes_despues.csv \
  --hourly-rate 25 \
  --ai-monthly 50 \
  --outdir paso-1-medir-ahorro-tiempo/results \
  --currency EUR


Salidas en results/:

kpis_por_tarea.csv → métricas por tarea + fila TOTAL

resumen_roi.md → resumen ejecutivo con:

Ahorro medio ponderado (min y %)

Coste base vs. coste IA total

Beneficio mensual estimado

ROI%

📊 KPIs sugeridos

Ahorro medio ponderado (min/%) por tarea

Horas liberadas/mes = (ahorro_minutos × volumen_mensual) / 60

Beneficio mensual por tarea y total

ROI% total

% de tareas con ROI% > 0 y % con ROI% > 50

✅ Control de calidad

Validar que minutos_despues ≤ minutos_antes

Revisar que todas las columnas sean numéricas y sin valores vacíos

volumen_mensual > 0 para promedios ponderados

Sensibilidad: probar --hourly-rate y --ai-monthly con ±20%

Identificar tareas con impacto desproporcionado (outliers)

🛠️ Solución de problemas

“No such file or directory” → revisar ruta en --input

NaN/Inf en resultados → hay celdas vacías o no numéricas

ROI% = NaN → coste_ia_total = 0; usar beneficio absoluto o definir coste mínimo

Beneficio negativo con ahorro positivo → la licencia/operación IA supera el ahorro; revisar ai-monthly o volumen

Resultados demasiado buenos → validar con cronometraje (time & motion), logs o muestreo manual
