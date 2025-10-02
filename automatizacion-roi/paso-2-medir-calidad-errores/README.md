# 📘 Paso 2 — Medir Calidad y Errores → CoPQ (*Cost of Poor Quality – Coste de la Mala Calidad*)

El segundo paso mide los **costes ocultos** que genera la mala calidad de los datos o procesos.
Se trata de cuantificar cuánto dinero pierde la empresa por **errores frecuentes**, tales como duplicados, direcciones incorrectas, contratos incompletos o facturación errónea.

Este análisis es fundamental porque el mayor coste en una organización no siempre es el tiempo perdido, sino los errores que generan pérdidas directas y reputacionales.

---

## 📦 Estructura de carpetas (local/repo)

```plaintext
automatizacionRoi/
└── paso-2-medir-calidad-errores/
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
```

---

## 📥 Datos de entrada

El cálculo parte de un archivo **CSV** con información sobre errores comunes:

- **tipo_error** → descripción breve del error.
- **frec_mensual** → cuántas veces ocurre al mes.
- **tiempo_correccion_min** → tiempo medio de corrección (en minutos).
- **coste_hora** → coste de la hora de la persona que corrige.
- **impacto_reputacional** → coste adicional asociado a cada error (multa, queja de cliente, devolución, etc.).

---

## 📝 Ejemplo de CSV

Archivo: `data_sample/errores_dataset.csv`

```csv
tipo_error,frec_mensual,tiempo_correccion_min,coste_hora,impacto_reputacional
Duplicados en base de clientes,25,10,25,50
Errores en direcciones de envío,15,12,25,30
Datos incompletos en contratos,8,20,30,80
Errores en facturación,5,25,40,100
```

---

## 🧮 Fórmulas utilizadas

Para cada error calculamos:

- **Coste de corrección** = (tiempo_correccion_min ÷ 60) × coste_hora × frec_mensual
- **Coste reputacional** = impacto_reputacional × frec_mensual
- **Coste total** = coste_correccion + coste_reputacional
- **Horas perdidas** = (tiempo_correccion_min × frec_mensual) ÷ 60

La fila `TOTAL` suma todos los valores y representa el **Coste de la Mala Calidad global (CoPQ)**.

---

## ▶️ Ejecución del script (una línea)

```bash
python automatizacionRoi/paso-2-medir-calidad-errores/scripts/compute_copq.py --input automatizacionRoi/paso-2-medir-calidad-errores/data_sample/errores_dataset.csv --outdir automatizacionRoi/paso-2-medir-calidad-errores/results
```

---

## 📊 Resultados esperados

El script genera dos salidas en la carpeta `results/`:

1. **`copq_por_error.csv`**
   - Contiene los cálculos por cada error y una fila `TOTAL`.
   - Incluye coste de corrección, reputacional, coste total y horas perdidas.

2. **`resumen_copq.md`**
   - Resumen ejecutivo con las principales métricas.

Ejemplo de salida (`resumen_copq.md`):

```markdown
# Resumen CoPQ
- **Coste total de la mala calidad (mensual):** 3182.50 EUR
- **Coste de corrección:** 342.50 EUR
- **Coste reputacional:** 2840.00 EUR
- **Horas perdidas al mes:** 11.9 h
```

---

## 📌 KPIs clave

- Coste total mensual de la mala calidad (CoPQ).
- Horas perdidas al mes por corrección de errores.
- % de errores que representan >50% del coste total (para priorización).
- Ranking de errores más costosos.

---

## ✅ Control de calidad

Antes de dar por válidos los resultados:
- Revisar que todas las columnas tengan valores positivos.
- Validar que `frec_mensual > 0`.
- Comprobar que no existan valores vacíos en el CSV.
- Revisar que un único error no concentre más del 70% del coste (posible outlier).

---

## 🛠️ Problemas frecuentes

- **NaN o errores en cálculo** → el CSV tiene valores vacíos o no numéricos.
- **Costes irreales** → impacto reputacional exagerado.
- **Resultados demasiado bajos** → frecuencia de errores mal estimada.
- **Resultados demasiado altos** → error con un coste desproporcionado (requiere validación).

---

## 📌 Conclusión

El **Paso 2** permite hacer visible el coste oculto de los errores.  
Con este método:
- Obtenemos un **ranking de errores más costosos**.
- Cuantificamos pérdidas en dinero y horas.
- Mostramos que la IA no solo ahorra tiempo (Paso 1), sino que también **reduce pérdidas ocultas**.

👉 Este es el segundo pilar de la automatización con ROI: demostrar que la IA tiene impacto positivo en eficiencia **y en calidad**.
