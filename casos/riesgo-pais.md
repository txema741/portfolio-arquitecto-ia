# Riesgo-País — Caso de Prompting Especializado (Nivel 1 descriptivo)

**Objetivo:** Evaluar el riesgo macro de un país para decisiones de entrada, inversión o exportación.  
**Rol del analista:** Evaluador de riesgo-país para negocio.

## 🧩 Contexto mínimo
- País (y región si procede)
- Sector/actividad a evaluar
- Horizonte temporal (0–3, 3–12, 12–36 meses)
- Exposición estimada (ventas, CAPEX/OPEX)

## 🧠 Prompt base (descriptivo)
Eres un **Analista de Riesgo-País**. Entrega:
1) **Panorama macro**: crecimiento, inflación, tipo de cambio, deuda.  
2) **Estabilidad política y social**, seguridad jurídica y regulatoria.  
3) **Riesgos externos**: balanza, commodities, geopolitica, desastres.  
4) **Riesgos financieros**: acceso a crédito, tipos, controles de capital.  
5) **Conclusión** con **semáforo de riesgo** (bajo/medio/alto) y **KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*)** de seguimiento.

> Expande siglas al primer uso: **CPI (*Consumer Price Index – Índice de Precios al Consumo*)**, **FX (*Foreign Exchange – Tipo de Cambio*)**, **FDI (*Foreign Direct Investment – Inversión Extranjera Directa*)**, **CDS (*Credit Default Swap – Permuta de Incumplimiento Crediticio*)**, **FSI (*Fragile States Index – Índice de Estados Frágiles*)**.

## 📥 Inputs sugeridos
- País, sector, nivel de exposición (volumen €), horizonte, apetito de riesgo.

## 📤 Salidas esperadas
- Resumen ejecutivo con semáforo  
- Cuadro de riesgos (macroeconómico, político, regulatorio, financiero, operativo)  
- Recomendaciones de mitigación y *go/no-go* preliminar  
- Lista de KPIs de vigilancia

## ⚠️ Problemas frecuentes (y mitigación)
1) **Datos desactualizados** → Señalar la fecha y rango; aportar fuentes alternativas.  
2) **Exceso de generalidad** → Aterrizar en el sector y *use case*.  
3) **Subestimar riesgo cambiario** → Simular escenarios de **FX** ±5–15%.  
4) **Sesgo optimista** → Añadir *worst case* y *stress test*.  
5) **Fuentes únicas** → Triangular con organismos y *think-tanks*.

## 📊 KPIs recomendados
- **CPI** interanual (%)  
- Deuda/PIB (%) y prima de riesgo (CDS 5Y)  
- Volatilidad **FX** (desviación mensual)  
- Flujo neto de **FDI** (% PIB)  
- **FSI** o índice de gobernanza relevante

## 🧪 Ejemplo breve
**País:** X (mercado emergente dependiente de *commodities*).  
**Riesgos claves:** Tipo de cambio volátil; presión inflacionaria; incertidumbre regulatoria sectorial.  
**Mitigaciones:** Cobertura **FX**, cláusulas de ajuste por inflación, *phasing* de inversión.  
**Semáforo:** Riesgo **medio-alto** a 12 meses; revisar trimestralmente los KPIs.
