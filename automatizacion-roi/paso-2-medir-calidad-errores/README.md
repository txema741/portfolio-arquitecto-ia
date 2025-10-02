# Paso 2 — Medir Calidad y Errores → CoPQ (*Cost of Poor Quality – Coste de la Mala Calidad*)

Este paso cuantifica el **impacto económico de los errores** en procesos o datasets.  
El objetivo es mostrar cómo la IA reduce los **costes ocultos** por correcciones, reprocesos o incumplimientos.

---

## 📦 Estructura del paso
```plaintext
paso-2-medir-calidad-errores/
├── README.md
├── requirements.txt
├── data_sample/
│   └── errores_dataset.csv
├── scripts/
│   └── compute_copq.py
├── results/
│   └── (copq_por_error.csv, resumen_copq.md)
└── tests/
    └── test_compute_copq.py

📥 Datos de entrada (CSV de ejemplo)

Guarda este archivo como data_sample/errores_dataset.csv:

tipo_error,frec_mensual,tiempo_correccion_min,coste_hora,impacto_reputacional
Duplicados en base de clientes,25,10,25,50
Errores en direcciones de envío,15,12,25,30
Datos incompletos en contratos,8,20,30,80
Errores en facturación,5,25,40,100

🧮 Fórmulas

coste_correccion = (tiempo_correccion_min / 60) × coste_hora × frec_mensual

coste_reputacional = impacto_reputacional × frec_mensual

coste_total = coste_correccion + coste_reputacional

CoPQ_total = Σ coste_total

▶️ Cómo ejecutar

Instalar dependencias:

pip install -r paso-2-medir-calidad-errores/requirements.txt


Ejecutar:

python paso-2-medir-calidad-errores/scripts/compute_copq.py \
  --input paso-2-medir-calidad-errores/data_sample/errores_dataset.csv \
  --outdir paso-2-medir-calidad-errores/results

📊 KPIs sugeridos

Coste total de corrección mensual (CoPQ).

% de cada error sobre el total.

Ranking Top 3 errores por coste.

Horas perdidas al mes.

✅ Control de calidad

Columnas numéricas (frec_mensual, tiempo_correccion_min, coste_hora, impacto_reputacional) deben ser > 0.

Revisar que el CoPQ_total no esté dominado por un único error (outlier).

🛠️ Solución de problemas

NaN en resultados → revisar CSV, hay celdas vacías.

Errores negativos → revisar que los costes y tiempos sean positivos.

Resultados irreales → validar si el impacto_reputacional es demasiado alto.

📄 requirements.txt
pandas>=2.0.0
numpy>=1.24.0
pytest>=7.4.0
