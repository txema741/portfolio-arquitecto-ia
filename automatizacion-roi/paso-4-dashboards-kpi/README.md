# 📂 Paso 4 – Automatización ROI  

## 🔹 Objetivo  
Implementar el **módulo de ejecución automatizada** que toma los resultados de los pasos anteriores (datos limpios, fórmulas aplicadas, KPIs validados) y los transforma en **informes estructurados y exportables** (Markdown, CSV y opcionalmente PDF).  

---

## 📥 Datos de Entrada  
- results/roi_kpis.csv → KPIs calculados en el paso 3.  
- results/quality_report.md → Informe de control de calidad.  
- data_sample/roi_input.csv → Dataset original.  

---

## 🖥️ Ejecución CLI  
python step_4_reporting/generate_reports.py \
  --input results/roi_kpis.csv \
  --quality results/quality_report.md \
  --outdir results/ \
  --pdf

### Parámetros disponibles  
- --input → CSV con los KPIs.  
- --quality → Informe de calidad generado en paso 3.  
- --outdir → Carpeta de salida (results/).  
- --pdf (opcional) → Exporta también un PDF.  

---

## 📊 Resultados Esperados  
1. final_report.md → Informe en Markdown con secciones:  
   - Resumen Ejecutivo  
   - KPIs con semáforos  
   - Gráficos de ROI  
   - Control de Calidad  
   - Conclusión  

2. final_report.csv → Tabla con KPIs finales (ROI, Payback, Margen, etc.).  

3. final_report.pdf (opcional) → Documento para clientes/directivos.  

---

## 📌 Ejemplo de Salida (final_report.md)  
# 📈 Informe ROI – Automatización (Paso 4)

## 1. Resumen Ejecutivo  
El análisis muestra que el proyecto alcanza un ROI del **22%** con un payback estimado de **14 meses**.  

## 2. KPIs con semáforos  
- ROI: 22% 🟢  
- Payback: 14 meses 🟡  
- Margen Neto: 18% 🟢  

## 3. Control de Calidad  
✔ Datos completos y validados  
✔ Fórmulas aplicadas correctamente  
❌ Una columna sin normalizar (detectada en Paso 3)  

## 4. Conclusión  
La inversión es **viable** bajo los escenarios actuales.  

---

## ✅ Control de Calidad  
- Verificar que se generan los tres formatos de salida (MD, CSV, PDF si procede).  
- Revisar que los semáforos de KPIs se asignen de forma coherente (verde ≥20%, amarillo 10–20%, rojo <10%).  
- Validar que el informe no presenta valores NaN.  

---

## ⚠️ Problemas Frecuentes  
- Error de permisos (Windows/WSL) → Ejecutar como administrador o revisar chmod +x en Linux.  
- Fallo de exportación a PDF → Asegurarse de tener reportlab instalado (pip install reportlab).  
- Columnas faltantes en input CSV → Revisar paso 3 antes de continuar.  

---

## 🎯 Conclusión del Paso 4  
Ya tenemos el módulo de reporting que consolida todos los resultados anteriores y los convierte en entregables listos para cliente/portafolio.  
El flujo ahora queda cerrado: entrada → limpieza → cálculo → informes.  


