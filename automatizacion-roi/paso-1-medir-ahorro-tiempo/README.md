# 📘 Paso 1 — Medir Ahorro de Tiempo → ROI (*Return on Investment – Retorno de la Inversión*)

Este primer paso tiene como objetivo comprobar si el uso de la IA realmente aporta beneficios medibles.
La forma más simple y universal es calcular **el ahorro de tiempo en tareas repetitivas** y transformarlo en **dinero**.
De esta forma obtenemos un **ROI (%)** claro, auditable y fácil de explicar.

---

## 📦 Estructura de carpetas (local/repo)

```plaintext
automatizacionRoi/
└── paso-1-medir-ahorro-tiempo/
    ├── README.md
    ├── requirements.txt
    ├── data_sample/
    │   └── tareas_antes_despues.csv
    ├── scripts/
    │   └── compute_roi.py
    ├── results/
    │   └── (kpis_por_tarea.csv, resumen_roi.md)
    └── tests/
        └── test_compute_roi.py
```

---

## 📥 Datos de entrada

El cálculo parte de un archivo **CSV** con información sobre cada tarea repetitiva:

- **tarea** → Nombre de la actividad.
- **minutos_antes** → Tiempo promedio (en minutos) que tardaba la tarea antes de usar IA.
- **minutos_despues** → Tiempo promedio después de usar IA.
- **volumen_mensual** → Número de veces que se realiza esa tarea al mes.

---

## 📝 Ejemplo de CSV

Archivo: `data_sample/tareas_antes_despues.csv`

```csv
tarea,minutos_antes,minutos_despues,volumen_mensual
Redacción de informe mensual,45,20,10
Limpieza de datos,30,12,20
Preparación de presentación,60,40,6
Revisión de contratos,35,28,15
```

Este archivo contiene **4 tareas comunes** en las que podemos observar el “antes” y “después” del uso de IA.

---

## 🧮 Fórmulas utilizadas

Para cada tarea calculamos:

- **Ahorro en minutos** = minutos_antes − minutos_despues
- **% de ahorro** = (ahorro ÷ minutos_antes) × 100
- **Coste original (sin IA)** = (minutos_antes × volumen_mensual × coste_hora) ÷ 60
- **Coste con IA (operativo)** = (minutos_despues × volumen_mensual × coste_hora) ÷ 60
- **Coste con IA (licencia)** = parte proporcional del coste mensual de la IA
- **Coste IA total** = coste_ia_operativo + coste_ia_licencia
- **Beneficio mensual** = coste_base − coste_ia_total
- **ROI (%)** = (beneficio ÷ coste_ia_total) × 100

La **fila TOTAL** agrega resultados globales:
- Promedios ponderados para minutos y % de ahorro.
- Sumas para costes y beneficio.
- ROI% global calculado a partir de totales.

---

## ▶️ Ejecución del script (una línea)

```bash
python automatizacionRoi/paso-1-medir-ahorro-tiempo/scripts/compute_roi.py --input automatizacionRoi/paso-1-medir-ahorro-tiempo/data_sample/tareas_antes_despues.csv --hourly-rate 25 --ai-monthly 50 --outdir automatizacionRoi/paso-1-medir-ahorro-tiempo/results --currency EUR
```

**Parámetros:**
- `--hourly-rate` → coste de la hora de trabajo (ejemplo: 25 €).
- `--ai-monthly` → coste mensual de la solución IA (ejemplo: 50 €).
- `--currency` → moneda de cálculo (ejemplo: EUR).

---

## 📊 Resultados esperados

El script genera dos salidas en la carpeta `results/`:

1. **`kpis_por_tarea.csv`**
   - Contiene los cálculos por cada tarea y una fila `TOTAL`.
   - Incluye ahorro en minutos, %, costes, beneficio y ROI.

2. **`resumen_roi.md`**
   - Resumen ejecutivo con los principales resultados.

Ejemplo de salida (`resumen_roi.md`):

```markdown
# Resumen ROI
- **Ahorro medio ponderado:** 16.4 min (44.2%)
- **Coste base mensual:** 806.25 EUR
- **Coste IA total mensual:** 508.33 EUR
- **Beneficio mensual:** 297.92 EUR
- **ROI%:** 58.6%
```

---

## 📌 KPIs clave

- Ahorro medio ponderado (en minutos y en %).
- Horas liberadas al mes.
- Beneficio mensual total.
- ROI% global.
- % de tareas con ROI positivo.

---

## ✅ Control de calidad

Antes de dar por válidos los resultados:
- Revisar que siempre `minutos_despues ≤ minutos_antes`.
- Verificar que `volumen_mensual > 0`.
- Confirmar que no haya valores vacíos o incorrectos en el CSV.
- Realizar pruebas de sensibilidad: cambiar `--hourly-rate` y `--ai-monthly` en ±20% para ver cómo varía el ROI.

---

## 🛠️ Problemas frecuentes

- **Archivo no encontrado** → revisar que la ruta al CSV sea correcta.
- **ROI = NaN** → ocurre si el coste IA total es 0.
- **Beneficio negativo** → significa que la IA cuesta más de lo que ahorra (revisar coste de licencia o volumen de tareas).
- **Resultados irreales** → revisar que los tiempos se hayan medido correctamente (cronómetro, logs o muestreo).

---

## 📌 Conclusión

El **Paso 1** convierte **minutos ahorrados en euros ahorrados**.
Con este método:
- Obtenemos un **ROI auditable**.
- Creamos un informe profesional y fácil de entender.
- Demostramos que la IA no es solo innovación, sino un **beneficio económico real**.

👉 Este es el primer cimiento de la automatización con ROI: una prueba clara que permite pasar a etapas más avanzadas.

