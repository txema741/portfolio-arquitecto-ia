# 📘 Paso 3 — Automatizaciones CLI (*Command Line Interface – Interfaz de Línea de Comandos*)

En este paso pasamos de análisis manual a **automatización real**.
El objetivo es que cualquier persona (consultor, analista, directivo) pueda lanzar cálculos de ROI o CoPQ **con un solo comando**, sin tener que abrir ni modificar código.

Esto se logra a través de **scripts con CLI** bien documentados.

---

## 📦 Estructura de carpetas (local/repo)

```plaintext
automatizacionRoi/
└── paso-3-automatizaciones-cli/
    ├── README.md
    ├── scripts/
    │   ├── run_roi.sh          # Script de automatización ROI
    │   ├── run_copq.sh         # Script de automatización CoPQ
    │   └── cli_launcher.py     # Opción avanzada: ejecutor unificado en Python
    └── tests/
        └── test_cli.py
```

---

## 📥 Datos de entrada

En este paso **reutilizamos** los CSV ya creados en el Paso 1 y Paso 2:
- `tareas_antes_despues.csv` para ROI.
- `errores_dataset.csv` para CoPQ.

No es necesario crear nuevos datasets, lo que cambia es la **forma de ejecutar y automatizar**.

---

## 🧮 Cómo funciona

1. Los scripts `.sh` (bash) permiten automatizar ejecución con parámetros preconfigurados.
2. El script `cli_launcher.py` permite elegir desde terminal qué cálculo ejecutar (ROI o CoPQ) y con qué parámetros.
3. Todo queda centralizado y reproducible → mismo input siempre genera mismo output.

---

## ▶️ Ejemplo de ejecución con Bash

### ROI
```bash
bash automatizacionRoi/paso-3-automatizaciones-cli/scripts/run_roi.sh
```

### CoPQ
```bash
bash automatizacionRoi/paso-3-automatizaciones-cli/scripts/run_copq.sh
```

Los `.sh` llaman internamente a los scripts de pasos anteriores (`compute_roi.py`, `compute_copq.py`) con rutas y parámetros ya preparados.

---

## ▶️ Ejemplo de ejecución con Python (CLI unificada)

Si usamos `cli_launcher.py`, la ejecución sería:

```bash
python automatizacionRoi/paso-3-automatizaciones-cli/scripts/cli_launcher.py roi --input automatizacionRoi/paso-1-medir-ahorro-tiempo/data_sample/tareas_antes_despues.csv --hourly-rate 25 --ai-monthly 50 --outdir automatizacionRoi/paso-1-medir-ahorro-tiempo/results --currency EUR
```

o bien para CoPQ:

```bash
python automatizacionRoi/paso-3-automatizaciones-cli/scripts/cli_launcher.py copq --input automatizacionRoi/paso-2-medir-calidad-errores/data_sample/errores_dataset.csv --outdir automatizacionRoi/paso-2-medir-calidad-errores/results
```

---

## 📊 Resultados esperados

- Informes (`resumen_roi.md`, `resumen_copq.md`) se generan automáticamente en sus carpetas correspondientes.
- Archivos CSV con métricas (`kpis_por_tarea.csv`, `copq_por_error.csv`).
- Logs de ejecución (opcional) para auditar cuándo y cómo se ejecutó el cálculo.

---

## 📌 KPIs clave

- Tiempo de ejecución de cada script.
- Frecuencia de uso de automatizaciones.
- % de usuarios que pueden ejecutar sin necesidad de tocar código.
- Reutilización de los mismos datasets sin inconsistencias.

---

## ✅ Control de calidad

- Verificar que las rutas usadas en los `.sh` y en `cli_launcher.py` sean correctas.
- Asegurar permisos de ejecución (`chmod +x run_roi.sh`).
- Comprobar que la salida se genere en la carpeta `results/`.
- Añadir pruebas automáticas (`test_cli.py`) que verifiquen que los scripts se ejecutan sin errores.

---

## 🛠️ Problemas frecuentes

- **Permiso denegado** → dar permisos a los `.sh` con `chmod +x archivo.sh`.
- **Ruta no encontrada** → revisar mayúsculas/minúsculas en nombres de carpetas.
- **Parámetros obligatorios faltantes** → el script CLI debe validarlos y dar mensajes claros.
- **Dependencias no instaladas** → usar `requirements.txt` desde los pasos anteriores.

---

## 📌 Conclusión

El **Paso 3** marca el inicio de la **automatización real**:
- Cualquier usuario puede lanzar los cálculos sin abrir ni modificar Python.
- Los procesos se vuelven **repetibles, auditables y rápidos**.
- Sentamos las bases para **dashboards automáticos** (Paso 4) y **orquestación avanzada** (Paso 5).

👉 Con este paso, pasamos de scripts aislados a **herramientas reproducibles de uso real en la empresa**.
