# Paso 2 — Medir Calidad y Errores → CoPQ (*Cost of Poor Quality – Coste de Mala Calidad*)

Este paso mide el impacto de los **errores y la calidad de los datos o procesos** en términos económicos. A partir de métricas de calidad, se calcula el **CoPQ** y su traducción a pérdidas evitables.

---

## 📦 Estructura del paso
```plaintext
paso-2-medir-calidad-errores/
├── README.md                      # Este archivo
├── requirements.txt               # Dependencias (pandas, numpy)
├── data_sample/
│   └── errores_registro.csv       # Datos de ejemplo
├── scripts/
│   └── compute_copq.py            # Script de cálculo
├── results/
│   └── (copq_por_dimension.csv, resumen_copq.md)
└── tests/
    └── test_compute_copq.py       # Tests mínimos (opcional)

📥 Datos de entrada

Archivo CSV de ejemplo (data_sample/errores_registro.csv):

dimension,total_registros,errores,impacto_unitario
Clientes,1000,50,20
Pedidos,500,25,15
Facturas,200,10,50


Esquema requerido:

dimension (texto) → Área analizada (clientes, pedidos, facturas, etc.)

total_registros (entero) → Nº de registros evaluados

errores (entero) → Nº de errores detectados

impacto_unitario (número) → Coste medio asociado a cada error (€)

)

🧮 Parámetros y fórmulas

Parámetros CLI del script compute_copq.py:

--input → ruta al CSV (ej: data_sample/errores_registro.csv)

--outdir → carpeta de salida (ej: results)

--currency → moneda (defecto: EUR)

Fórmulas por dimensión:

error_rate = errores / total_registros

coste_errores = errores × impacto_unitario

copq_pct = (coste_errores / (total_registros × impacto_unitario)) × 100 (aprox. del % coste por calidad pobre)

Fórmulas totales:

errores_totales = Σ errores

coste_total_errores = Σ coste_errores

error_rate_global = errores_totales / Σ total_registros

▶️ Cómo ejecutar
# Instalar dependencias
pip install -r paso-2-medir-calidad-errores/requirements.txt

# Ejecutar cálculo
python paso-2-medir-calidad-errores/scripts/compute_copq.py \
  --input paso-2-medir-calidad-errores/data_sample/errores_registro.csv \
  --outdir paso-2-medir-calidad-errores/results \
  --currency EUR


Salidas en results/:

copq_por_dimension.csv → Métricas de CoPQ por cada dimensión

resumen_copq.md → Resumen ejecutivo con:

Tasas de error por dimensión y global

Coste estimado de la mala calidad

% de pérdida sobre el total

📊 KPIs sugeridos

Tasa de error por dimensión = errores / total_registros

Errores totales detectados

Coste económico por errores (€)

CoPQ % sobre volumen total

Reducción de errores tras IA (comparativa antes/después)

✅ Control de calidad

Validar que errores ≤ total_registros

Revisar que impacto_unitario ≥ 0

Evitar columnas vacías o valores no numéricos

Comprobar que la suma global de errores coincide con el detalle por dimensión

Hacer pruebas de sensibilidad cambiando impacto_unitario ±20%

🛠️ Solución de problemas

“No such file or directory” → revisar ruta en --input

Valores negativos → revisar campos errores e impacto_unitario

Tasas >100% → verificar coherencia errores ≤ total_registros

Resultados nulos → puede que errores = 0; en ese caso, el CoPQ es 0%

Costes incoherentes → validar impacto_unitario con fuentes del negocio (ej: coste por retrabajo, penalizaciones, reclamaciones)


