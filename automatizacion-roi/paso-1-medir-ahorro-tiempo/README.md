# 📘 Paso 1 — Medir Ahorro de Tiempo → ROI (*Return on Investment – Retorno de la Inversión*)

Este primer paso busca **demostrar con datos** si la Inteligencia Artificial realmente está generando beneficios.  
Lo hacemos de la forma más sencilla y universal: **medir cuánto tiempo ahorramos en tareas repetitivas** y traducir ese ahorro en **dinero**.

En otras palabras:
1. Antes de usar IA, una tarea nos lleva **X minutos**.  
2. Después de usar IA, la misma tarea nos lleva **menos tiempo**.  
3. Si sabemos cuántas veces al mes hacemos esa tarea y cuánto cuesta la hora de trabajo → podemos calcular **el dinero ahorrado**.  
4. Con ese dato, calculamos el **ROI (Retorno de la Inversión)** y tenemos un informe económico claro para tomar decisiones.

---

## 🎯 ¿Por qué este paso es importante?
- Es un **mínimo producto viable (MVP)**: rápido, sencillo y entendible por cualquiera.  
- Permite **justificar ante dirección** que la IA no es “magia”, sino ahorro medible.  
- Genera un **primer informe auditable**, con números fáciles de comprobar.  
- Crea confianza para pasar a pasos más avanzados (calidad, automatización, dashboards).  

---

## 📦 Estructura del paso
```plaintext
paso-1-medir-ahorro-tiempo/
├── README.md                # Esta explicación
├── requirements.txt         # Dependencias (pandas, numpy, pytest)
├── data_sample/
│   └── tareas_antes_despues.csv   # Dataset de ejemplo
├── scripts/
│   └── compute_roi.py       # Script de cálculo
├── results/
│   └── (kpis_por_tarea.csv, resumen_roi.md)
└── tests/
    └── test_compute_roi.py  # Prueba automática (opcional)

📥 Datos de entrada: ¿qué información necesitamos?

El dataset de entrada (tareas_antes_despues.csv) contiene una lista de tareas repetitivas con 3 datos básicos:

minutos_antes → cuánto tardaba la tarea antes de usar IA.

minutos_despues → cuánto tarda con IA.

volumen_mensual → cuántas veces al mes repetimos la tarea.

Ejemplo:

tarea,minutos_antes,minutos_despues,volumen_mensual
Redacción de informe mensual,45,20,10
Limpieza de datos,30,12,20
Preparación de presentación,60,40,6
Revisión de contratos,35,28,15

🧮 Fórmulas explicadas de forma simple

Imagina que eres el responsable de operaciones y quieres cuantificar el ahorro.
Para cada tarea calculamos:

Minutos ahorrados = minutos_antes − minutos_despues

% de ahorro = (minutos ahorrados ÷ minutos_antes) × 100

Coste original = tiempo antes × coste hora × volumen mensual

Coste con IA = tiempo después × coste hora × volumen mensual + coste proporcional de la licencia IA

Beneficio = coste original − coste con IA

ROI (%) = (beneficio ÷ coste con IA) × 100

👉 En resumen: ¿cuánto dinero me ahorra la IA comparado con lo que me cuesta?

▶️ Ejecución en una sola línea

Una vez configurado Python y dependencias:

python automatizacionRoi/paso-1-medir-ahorro-tiempo/scripts/compute_roi.py --input automatizacionRoi/paso-1-medir-ahorro-tiempo/data_sample/tareas_antes_despues.csv --hourly-rate 25 --ai-monthly 50 --outdir automatizacionRoi/paso-1-medir-ahorro-tiempo/results --currency EUR


Donde:

--hourly-rate = coste de la hora de trabajo (ej: 25 €).

--ai-monthly = coste mensual de la IA (ej: 50 €).

--currency = moneda (EUR, USD…).

📊 Resultados que obtendrás

Archivo CSV (kpis_por_tarea.csv) → con todos los cálculos por tarea y una fila final con los totales.

Cuánto tiempo ahorra cada tarea.

Cuánto dinero se ahorra.

ROI por tarea y global.

Resumen en Markdown (resumen_roi.md) → un informe ejecutivo listo para enviar:

Ejemplo de salida:

# Resumen ROI
- **Ahorro medio ponderado:** 16.4 min (44.2%)
- **Coste base mensual:** 806.25 EUR
- **Coste IA total mensual:** 508.33 EUR
- **Beneficio mensual:** 297.92 EUR
- **ROI%:** 58.6%

✅ Control de calidad y buenas prácticas

Verifica que siempre minutos_despues ≤ minutos_antes.

Asegúrate de que volumen_mensual > 0.

Si los resultados parecen “demasiado buenos”, revisa que los tiempos medidos sean reales.

Haz pruebas de sensibilidad: cambia el coste de hora o la licencia en ±20% para ver si el ROI sigue siendo positivo.

🛠️ Problemas comunes

“No such file or directory” → revisa que la ruta al CSV es correcta.

ROI = NaN → pasa si el coste IA total es cero (p.ej., --ai-monthly 0).

Beneficio negativo → significa que la IA cuesta más de lo que ahorra → replantear volumen, prompts o plan de licencia.

Resultados poco claros → añade más tareas y volumen para mayor robustez.

📌 Conclusión del Paso 1

En este paso:

Tradujimos minutos ahorrados → euros ahorrados.

Creamos un ROI% simple y defendible.

Obtuvimos un primer informe auditable que cualquier directivo puede leer.

👉 Con esto ya tenemos el primer bloque sólido de la Fase 2: demostrar con datos concretos que la IA no solo es “innovación”, sino valor económico real.

