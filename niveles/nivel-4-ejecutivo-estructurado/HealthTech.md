# Nivel 4 — Estratégico (HealthTech)

## ROL Y TONO
Actúa como **consultor regulatorio senior en HealthTech y dispositivos médicos de IA, con 15+ años de experiencia en CE-marking, GDPR sanitario y ciberseguridad hospitalaria**.  
Estilo: **contundente, ejecutivo, orientado a gestión hospitalaria**.

## CASO Y ALCANCE
- Caso: Hospital de Madrid implementa sistema de **IA radiológica diagnóstica** (2025).  
- Sector: HealthTech / IA en diagnóstico clínico.  
- Jurisdicción/Ámbito: UE (MDR 2017/745, GDPR art. 9, NIS2, HL7/FHIR interoperabilidad).  
- Fecha de referencia: 2025-10-01.

## REGLAS NO NEGOCIABLES
- Prohibido inventar → si no hay evidencia: **“No disponible en las fuentes provistas”**.  
- Vigencia: normativa consolidada; si duda → **“Vigencia no confirmada”**.  
- Trazabilidad: numerar *claims*, citar Art./§ + URL/ID. Confianza (1–5). ⚠️ si ≤2.  
- Protección de datos y ética IA: GDPR art. 9, UNESCO 2021, Directrices UE 2019.  
- Concisión estricta.

## FUENTES AUTORIZADAS
- EMA (https://www.ema.europa.eu/)  
- Diario Oficial de la UE (https://eur-lex.europa.eu/)  
- Agencia Española de Medicamentos (https://www.aemps.gob.es/)  

---

## SALIDAS — FORMATO OBLIGATORIO

### 1. Resumen Ejecutivo (≤180 palabras, 5 viñetas numeradas)
1. **Certificación CE (MDR arts. 52–54)**: retraso ≥12m si los ensayos no cumplen requisitos multicéntricos.  
2. **Protección de datos clínicos (GDPR art. 9)**: riesgo de sanciones del 4 % turnover y pérdida de confianza.  
3. **Sesgo clínico IA**: falsos negativos en subgrupos poblacionales → riesgo reputacional y legal.  
4. **Ciberseguridad hospitalaria (NIS2)**: paros de 48h generan impacto clínico y financiero grave.  
5. **Interoperabilidad limitada (HL7/FHIR)**: +20 % costes ocultos de integración y resistencia clínica.

---

### 2. Matriz Técnica — 5 Riesgos
| # | Riesgo | Norma/Art. | Jurisdicción | Evidencia | Impacto | Prob. | Nivel | Mitigación (3) | Confianza |
|---|--------|------------|--------------|-----------|---------|-------|-------|----------------|-----------|
| 1 | Certificación CE retrasada | MDR Arts. 52–54 | UE | CELEX 32017R0745 | Coste +1 M€, retraso ≥12m | Media | Alto | • Pre-consulta AEMPS • Ensayos multicéntricos • Documentación robusta | 4 |
| 2 | Protección de datos clínicos | GDPR Arts. 9, 32 | UE | CELEX 32016R0679 | Multa hasta 4 % turnover | Media | Alto | • DPIA • Anonimización • Seguridad reforzada | 5 |
| 3 | Sesgo clínico IA | MDR + UE AI Ethics 2019 | UE | COM(2019)168 | Diagnóstico desigual, litigios | Baja-Media | Medio | • Dataset diverso • Auditoría ética • Supervisión humana | 4 |
| 4 | Ciberseguridad hospitalaria | NIS2 Arts. 21–23 | UE | CELEX 32022L2555 | Interrupción 48h, riesgo pacientes | Alta | Alto | • SOC hospitalario • Backups cifrados • DRP | 4 |
| 5 | Interoperabilidad | HL7/FHIR + MDR | UE | HL7 Standards EU | Coste +20 %, rechazo clínico | Media | Medio | • APIs estandarizadas • Test integraciones • Vendor neutral | 3 |

---

### 3. Escenarios O/R/P
- **Optimista (O):** Certificación CE en 6m, interoperabilidad plena, adopción clínica ≥80 %.  
- **Realista (R):** Certificación CE en 12m, interoperabilidad parcial, adopción 60 %.  
- **Pesimista (P):** Retraso >18m, ciberataque, adopción <40 %, ROI negativo.  

---

### 4. Plan de Acción 7×7
| Acción | Responsable | Días | KPI |
|--------|-------------|------|-----|
| A1. Pre-consulta CE MDR | Regulatory Affairs | 30 | Feedback AEMPS recibido |  
| A2. DPIA y anonimización | DPO hospital | 60 | DPIA validado |  
| A3. Auditoría sesgo IA | Comité ético IA | 90 | Informe sesgo aprobado |  
| A4. Implementar SOC hospitalario | CISO | 120 | SOC activo 24/7 |  
| A5. Test interoperabilidad HL7/FHIR | IT hospital + vendor | 120 | % integraciones exitosas |  
| A6. Plan formación clínica | Dirección médica | 180 | ≥70 % médicos capacitados |  
| A7. Evaluación roadmap ESG sanitario | Comité ESG | 180 | Informe publicado |  

---

### 5. Checklist Ético-Legal
1. MDR certificación CE ✅  
2. GDPR DPIA clínico ✅  
3. Consentimiento informado pacientes ✅  
4. NIS2 plan ciberseguridad ✅  
5. Auditoría sesgo IA ⚠️  
6. Interoperabilidad HL7/FHIR ✅  
7. Supervisión comité ético ✅  
8. Informe ESG sanitario ⚠️  
9. Seguridad clínica DRP ✅  
10. Transparencia en reporting ✅  

---

### 6. Metadatos y QA
- Fuentes: EMA, EUR-Lex, AEMPS.  
- Contradicciones: interoperabilidad HL7/FHIR según vendor.  
- “No disponible” en métricas ESG hospitalarias.  
- Confianza media: 4/5.  
- Fecha revisión: 2025-10-01.

---

## ⚠️ Problemas del Nivel 4
- No incluye comparativa con hospitales líderes internacionales.  
- ESG y métricas de impacto social poco desarrolladas.  
- Seguimiento aún basado en informes estáticos.

## 🆙 Por qué N5 es mejor
- Dashboards clínicos en tiempo real (AUC, TAT, tasa error diagnóstico).  
- Simulación *what-if* (ciberataque, retraso CE, adopción clínica).  
- Integración ESG + telemetría viva hospitalaria.

## 🔎 Observaciones
El N4 en HealthTech es **clave para comités directivos hospitalarios y reguladores**, pues convierte riesgos regulatorios y técnicos en un **plan estratégico con responsables, plazos y KPIs**.  
Permite anticipar problemas de certificación, datos clínicos y ciberseguridad, y ofrece una ruta clara hacia la adopción.  
Sin embargo, sigue siendo un **documento estático** que no captura variaciones en tiempo real ni compara con **mejores prácticas internacionales**.  
El N5 cubrirá esa brecha, convirtiendo este análisis en un **sistema vivo de soporte a la decisión clínica**.  
