# 📘 Paso 4 — Dashboards KPI (*Key Performance Indicators – Indicadores Clave de Desempeño*)

En este paso transformamos los resultados obtenidos (ROI y CoPQ) en **dashboards visuales** que permiten a los directivos y equipos ver de forma clara el impacto de la IA.

El objetivo es pasar de **números en CSV/Markdown** a **gráficos interactivos y fáciles de entender**.

---

## 📦 Estructura de carpetas (local/repo)

```plaintext
automatizacionRoi/
└── paso-4-dashboards-kpi/
    ├── README.md
    └── dashboards/
        ├── roi_dashboard.ipynb       # Notebook ROI con visualización
        ├── copq_dashboard.ipynb      # Notebook CoPQ con visualización
        └── kpi_dashboard_powerbi.pbix # Ejemplo en Power BI
```

---

## 📥 Datos de entrada

- Resultados de pasos anteriores:
  - `results/kpis_por_tarea.csv` (Paso 1).
  - `results/copq_por_error.csv` (Paso 2).
- Archivos se importan en notebooks o en Power BI.

---

## 🧮 Cómo funciona

1. Los datos de ROI y CoPQ se cargan desde CSV.
2. Se transforman en métricas clave: ROI global, CoPQ total, ahorro horas, ranking errores.
3. Se generan visualizaciones:
   - **Gráficos de barras** → tareas/errores más costosos.
   - **Gráficos de líneas** → evolución mensual del ROI.
   - **Semáforos KPI** → verde (>50% ROI), ámbar (0-50%), rojo (<0).

---

## ▶️ Ejemplo de ejecución

### Jupyter Notebook
```bash
jupyter notebook automatizacionRoi/paso-4-dashboards-kpi/dashboards/roi_dashboard.ipynb
```

### Power BI
Abrir `kpi_dashboard_powerbi.pbix` e importar los CSV desde `results/`.

---

## 📊 Resultados esperados

- Dashboard ROI mostrando ahorro total y ROI% por tarea.
- Dashboard CoPQ mostrando errores más costosos y pérdidas mensuales.
- Dashboard combinado con indicadores globales.

---

## 📌 KPIs clave

- ROI% global.
- Beneficio mensual total (€).
- Coste total de errores (CoPQ).
- Horas liberadas/mes.
- % de errores críticos corregidos.

---

## ✅ Control de calidad

- Validar que los dashboards usan **los mismos datos** que los cálculos originales.
- Verificar que los KPIs se actualizan al refrescar los datos.
- Revisar que los gráficos tienen escalas correctas.

---

## 🛠️ Problemas frecuentes

- **Datos no se cargan** → revisar rutas de los CSV.
- **Gráficos vacíos** → columnas con nombres distintos a los esperados.
- **Inconsistencia en valores** → CSV sin actualizar tras nueva ejecución.

---

## 📌 Conclusión

El **Paso 4** convierte cálculos en **insights visuales**.
Esto permite que los directivos entiendan el impacto de la IA de forma inmediata y facilita la toma de decisiones basadas en datos.
