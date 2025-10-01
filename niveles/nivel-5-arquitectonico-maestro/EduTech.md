# Nivel 5 — Ejecutivo (EduTech / Docencia)

## ROL Y TONO
Actúa como **consultor senior en políticas educativas e IA en aula (UE/ES) con 15+ años**. Estilo **ejecutivo, ético y verificable**.

## PROPÓSITO
Informe auditable para una **red de colegios** que implanta **IA generativa** (tutoría/personalización), con foco en **GDPR/LOPDGDD, ePrivacy, UNESCO 2021, NIS2**.

## ENTRADAS
- Caso: 25 centros, 30.000 alumnos, España-UE.  
- Fuentes: BOE (LOPDGDD), EUR-Lex (GDPR/ePrivacy/NIS2), UNESCO, EC Educación Digital.  
- Fecha: 2025-10-01.

## REGLAS NO NEGOCIABLES
Igual que FinTech (anti-alucinación, trazabilidad, vigencia, conflictos, confidencialidad).

## SALIDAS

### 1) Resumen Ejecutivo (≤250 palabras)
Top-5: **(1) Protección de menores (GDPR art. 8 / LOPDGDD)**; **(2) Inclusión/brecha digital**; **(3) Sesgo/ética IA (UNESCO 2021)**; **(4) Cambio cultural docente/capacitación**; **(5) Ciber/NIS2 (datos alumnos/CRM/LMS)**.  
Mitigaciones: **DPIA** y consentimiento parental reforzado, **programa de becas y dispositivos**, **auditoría de sesgo** y supervisión docente, **formación por niveles/incentivos**, **plan NIS2** (copias, DRP, *zero-trust*). O/R/P + sensibilidad y *dashboard*.

### 2) Tabla Técnica
| # | Riesgo | Norma/Indicador | Jurisdicción | Evidencia | Impacto | Prob. | Mitigación (3) | Conf. |
|---|--------|------------------|--------------|-----------|---------|-------|----------------|------|
| 1 | Datos de menores (consentimiento) | **GDPR art. 8; LOPDGDD** | UE/ES | BOE/EUR-Lex | Multas; retirada contenidos | Media | Alto | DPIA; verificación parental; minimización | 5 |
| 2 | Brecha digital | **EC Digital Education** | UE | EC | Exclusión 10–15% | Media | Alto | Becas; préstamo; conectividad | 4 |
| 3 | Sesgo/ética IA | **UNESCO 2021** | Global | UNESCO | Reputación; desigualdades | Media | Medio | Auditoría; datasets inclusivos; *human-in-loop* | 4 |
| 4 | Adopción docente | **OCDE TALIS** | Global | OCDE | Bajo uso de IA | Alta | Medio | Formación; incentivos; *peer mentoring* | 3 |
| 5 | Ciber/NIS2 | **NIS2** | UE | ENISA | Brechas; sanciones | Media | Medio | DRP; *zero-trust*; monitorización | 3 |

### 3) O/R/P
O: adopción ≥70%; brecha ≤5%; mejora rendimiento +15% | R: 50%; 10%; +8% | P: <30%; 15%; −10%

### 4) Sensibilidad (legal→financiera/impacto, **vinculada**)
**Supuestos**: coste/alumno __ €; adopción docente __ %; becas __ €; horizonte __ meses.  
- **Consentimiento parental −X pp** → **R#1** → **ΔCobertura [__, __] / ΔIngresos [__, __] / ΔNPV [__, __]**  
- **Brecha +Y%** → **R#2** → **ΔRendimiento/Coste becas / ΔNPV**  
- **Sesgo IA detectado** → **R#3** → **ΔCoste corrección/ reputación (proxy) / ΔNPV**  
- **Adopción docente −Z pp** → **R#4** → **ΔResultados / Retención / ΔNPV**  
- **Incidente NIS2** → **R#5** → **ΔCoste respuesta / Multas / ΔNPV**  
- **Tipos +150 pb (WACC o tasa social de descuento)** → **Risk Multiplier (no riesgo legal primario)**: **amplifica el impacto** en NPV de todos → **ΔNPV [__, __]**  
> Si no se puede calcular: `calc_status: degradado`. Marcar inferencias con leyenda y Confianza ≤2.

### 5) Dashboard (semáforos + mapping)
**Semáforos:** Consentimiento parental: 🟢 ≥90% · 🟠 75–90% · 🔴 <75% | Brecha digital: 🟢 ≤5% · 🟠 5–10% · 🔴 >10% | Sesgo IA (hallazgos críticos): 🟢 0 · 🟠 1 · 🔴 ≥2 | Adopción docente: 🟢 ≥70% · 🟠 50–70% · 🔴 <50% | Incidentes NIS2: 🟢 0–1 · 🟠 2–3 · 🔴 >3

| KPI | Fuente | Valor | Umbral | Estado |
|-----|--------|-------|--------|--------|
| Consentimiento parental (GDPR) | DPO | __ % | 🟢 ≥90 · 🟠 75–90 · 🔴 <75 | 🟢/🟠/🔴 |
| Brecha digital | Dirección | __ % | 🟢 ≤5 · 🟠 5–10 · 🔴 >10 | 🟢/🟠/🔴 |
| Hallazgos de sesgo IA | Comité Ético | __ | 🟢 0 · 🟠 1 · 🔴 ≥2 | 🟢/🟠/🔴 |
| Adopción docente IA | Rectorado | __ % | 🟢 ≥70 · 🟠 50–70 · 🔴 <50 | 🟢/🟠/🔴 |
| Incidentes críticos NIS2 | CISO | __ | 🟢 0–1 · 🟠 2–3 · 🔴 >3 | 🟢/🟠/🔴 |

**Mapping:** Consentimiento→R#1 | Brecha→R#2 | Sesgo→R#3 | Adopción→R#4 | NIS2→R#5 | **Tipos +150 pb**→*Risk Multiplier*

### 6) Checklist (10)
DPIA menores ✅ · Consentimiento parental ✅ · Inclusión/becas ✅ · Auditoría sesgo IA ✅ · Supervisión docente ✅ · NIS2 DRP ✅ · Accesibilidad digital ✅ · Transparencia métricas ✅ · Políticas de datos ✅ · Confidencialidad ✅

### 7) Metadatos y QA
Fuentes: BOE, EUR-Lex, UNESCO, EC, ENISA | *Gates* y Anti-Alucinación aplicados | Confianza media ≥4/5 | Fecha 2025-10-01

## MÓDULOS
Registro de Claims | Rúbrica | Gates | Contradicciones | Runbook “No disponible” | Hooks: **GDPR/LOPDGDD**, **UNESCO**, **NIS2**, **accesibilidad**, **ESG educativo**.
