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


