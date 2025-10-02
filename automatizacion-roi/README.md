# 📘 Paso 5 — Orquestación (*ETL – Extract, Transform, Load*)

El último paso consiste en **orquestar todos los procesos** (ROI, CoPQ, dashboards) para que se ejecuten de forma automática y programada.

Esto asegura que la información siempre esté actualizada y que el flujo completo sea **robusto y escalable**.

---

## 📦 Estructura de carpetas (local/repo)

```plaintext
automatizacionRoi/
└── paso-5-orquestacion/
    ├── README.md
    └── pipelines/
        ├── etl_roi.py         # Pipeline de ROI
        ├── etl_copq.py        # Pipeline de CoPQ
        ├── master_pipeline.py # Orquestador principal
        └── crontab_example.txt # Ejemplo de ejecución automática
```

---

## 📥 Datos de entrada

- Archivos de datos iniciales (CSV de tareas y errores).
- Scripts de cálculo ROI y CoPQ de pasos anteriores.
- Dashboards KPI creados en el Paso 4.

---

## 🧮 Cómo funciona

1. **Extract** → toma datasets de entrada (CSV o base de datos).
2. **Transform** → aplica scripts de ROI y CoPQ.
3. **Load** → guarda resultados en `results/` y actualiza dashboards.
4. **Orquestación** → `master_pipeline.py` ejecuta todo en orden.

Opciones de automatización:
- **Crontab** en Linux.
- **Task Scheduler** en Windows.
- **Airflow o Prefect** para proyectos más avanzados.

---

## ▶️ Ejemplo de ejecución

```bash
python automatizacionRoi/paso-5-orquestacion/pipelines/master_pipeline.py
```

Si se quiere automatizar cada día a las 8:00, se añade a `crontab` en Linux:

```bash
0 8 * * * python /ruta/automatizacionRoi/paso-5-orquestacion/pipelines/master_pipeline.py
```

---

## 📊 Resultados esperados

- Ejecución automática de ROI y CoPQ.
- Generación de dashboards siempre actualizados.
- Reportes listos para dirección sin intervención manual.

---

## 📌 KPIs clave

- Tiempo total del pipeline.
- Frecuencia de actualización de dashboards.
- % de ejecuciones exitosas.
- Reducción del esfuerzo manual.

---

## ✅ Control de calidad

- Probar el pipeline primero manualmente.
- Asegurar que los errores se registran en logs.
- Verificar que los resultados se guardan siempre en `results/`.

---

## 🛠️ Problemas frecuentes

- **Scripts no encontrados** → revisar rutas.
- **Errores de permisos** → configurar permisos en servidor.
- **Jobs no se ejecutan** → verificar configuración de crontab o scheduler.

---

## 📌 Conclusión

El **Paso 5** convierte el flujo de trabajo en un **sistema orquestado**.
Con esto, la empresa pasa de cálculos aislados a una solución de IA **escalable, automática y mantenible**, lista para un entorno real.
