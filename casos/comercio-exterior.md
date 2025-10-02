# Comercio Exterior — Caso de Prompting Especializado (Nivel 1 descriptivo)

**Objetivo:** Guiar una operación de exportación/importación con visión integral (aranceles, logística, contratos, riesgo).  
**Rol del analista:** Consultor de comercio internacional para PYMEs.

## 🧩 Contexto mínimo
- Producto y **HS Code (*Harmonized System – Sistema Armonizado*)**
- Origen y destino
- Incoterm recomendado
- Volumen y frecuencia (envíos/mes)
- Sensibilidades: perecedero, peligroso (IMO), control dual, temperatura

## 🧠 Prompt base (descriptivo)
Eres un **Evaluador de Operaciones de Comercio Exterior**. Entrega:
1) Requisitos clave por **aduanas** (licencias, certificaciones, etiquetado).  
2) Estimación de **costes logísticos** (flete, seguro, manipulación) y **lead times**.  
3) **Aranceles e impuestos** aplicables (si no hay dato, indica fuentes verificables).  
4) Riesgos operativos y contractuales según **Incoterms®**.  
5) **KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*)** para control mensual.

> Expande siglas al primer uso: **LPI (*Logistics Performance Index – Índice de Desempeño Logístico*)**, **CPI (*Consumer Price Index – Índice de Precios al Consumo*)**, **GPI (*Global Peace Index – Índice de Paz Global*)**, **SLA (*Service Level Agreement – Acuerdo de Nivel de Servicio*)**, **OTIF (*On Time In Full – A Tiempo y Completo*)**.

## 📥 Inputs sugeridos
- Producto + HS, origen/destino, Incoterm, embalaje, requisitos del cliente, tolerancia a lead time, valor FOB/CIF.

## 📤 Salidas esperadas
- Checklist documental por aduana  
- Escandallo de costes estimados (rango)  
- Matriz de riesgos por eslabón (fábrica, puerto, tránsito, destino)  
- KPIs operativos y de servicio (con objetivos)

## ⚠️ Problemas frecuentes (y mitigación)
1) **HS incorrecto** → Validar con arancelario oficial y *broker* local.  
2) **Incoterm mal elegido** → Alinear responsabilidades, seguros y punto de entrega.  
3) **Costes “optimistas”** → Usar rangos y añadir recargos (BAF, GRI) si aplica.  
4) **Tiempos sin buffer** → Incluir buffers por congestión/inspecciones.  
5) **Falta de trazabilidad** → Definir eventos y EDI/actualizaciones obligatorias.

## 📊 KPIs recomendados
- **OTIF** %  
- Lead time puerta-a-puerta (p50/p90)  
- % desvío coste real vs. estimado  
- Daños/mermas por 1.000 unidades  
- Demoras y sobreestadías (días/coste)

## 🧪 Ejemplo breve
**Operación:** Exportar maquinaria **HS 8479** de España a México con **Incoterm DAP (*Delivered At Place – Entregado en Lugar*)**.  
**Checklist:** Factura, *packing list*, certificado de origen si aplica, seguro, registro importador.  
**Costes (rango):** Flete marítimo 40’HC, seguro 0,5–1,0% **CIF (*Cost, Insurance and Freight – Costo, Seguro y Flete*)**, *handling* en destino.  
**KPIs:** OTIF ≥ 95%, lead time ≤ 32 días p90, desviación de coste ≤ 8%.
