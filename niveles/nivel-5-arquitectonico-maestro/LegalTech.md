# Nivel 5 — Ejecutivo (LegalTech)

## PROPÓSITO  
Desarrollar un **sistema experto autónomo en M&A LegalTech**, capaz de generar un **informe auditable, dinámico y ético** para el consejo de administración.  
Debe operar con **dashboards en tiempo real**, simulaciones *what-if* y métricas auditables.  
⚠️ SIN inventar datos → usar solo fuentes autorizadas; en caso contrario → **“No disponible en las fuentes provistas”**.

---

## ENTRADAS
- Caso: Fusión entre dos empresas de software en España (150 M€).  
- Sector: LegalTech / M&A tecnológico.  
- Jurisdicciones (prioridad 1→3): España, UE, Internacional (CNMC, TJUE, CIADI).  
- Fuentes autorizadas: CNMC, BOE (LSC), EUR-Lex (Directiva UE), EDPB (GDPR), ENISA (NIS2).  
- Fecha de referencia: 2025-10-01.  
- Audiencias: Consejo Directivo / Área Técnica-Legal / Comité Ético-ESG.  

---

## REGLAS NO NEGOCIABLES
1. **No inventes** → si no hay evidencia: *“No disponible en las fuentes provistas”*.  
2. **Vigencia** → usar solo normativa consolidada; si hay duda: *“Vigencia no confirmada”*.  
3. **Protección de datos** → GDPR, LOPDGDD, ePrivacy.  
4. **Ética IA** → UNESCO 2021; Directrices UE 2019.  
5. **Trazabilidad absoluta** → numerar *claims*, Art./§ + URL/ID, confianza (1–5), ⚠️ si ≤2.  
6. **Conflictos normativos** → resolver por lex specialis / lex posterior / jerarquía.  
7. **Confidencialidad** → no exponer PII/PHI sin anonimización.  

---

## FASES
- **F1. Delimitación** → alcance, límites y supuestos clave.  
- **F2. Identificación** → lista ampliada de riesgos (jurídicos, regulatorios, PI, ciber).  
- **F3. Validación** → anclaje a artículos y fuentes verificadas.  
- **F4. Contradicciones** → resolución metodológica.  
- **F5. Priorización** → matriz Impacto × Probabilidad; selección Top-5.  
- **F6. Redacción por audiencia** →  
   - Directivo: ≤250 palabras, tono ejecutivo.  
   - Técnica-Legal: tabla validada.  
   - Ética/ESG: checklist.  
- **F7. Control de calidad** → claims sin fuente = bloqueados; confianza ≤2 → ⚠️ justificado.  

---

## SALIDAS (MARKDOWN)

### 1. Resumen Ejecutivo (≤250 palabras)
Informe legal estratégico sobre la fusión, con **estado regulatorio, riesgos priorizados y simulaciones financieras**.  
Enfatiza trazabilidad de normativa, riesgos de nulidad, sanciones CNMC, protección de datos y ciberseguridad.  

---

### 2. Tabla Técnica (Top-5 Riesgos)
| Riesgo | Norma/Art. | Jurisdicción | Evidencia | Impacto | Prob. | Nivel | Mitigación (3) | Confianza |
|--------|------------|--------------|-----------|---------|-------|-------|----------------|-----------|
| Competencia | LDC Art. 2, 8, 10 | España | CNMC Resol. S/DC/0598/17 | Multa 10 % ingresos | Media | Alto | • Notificación CNMC • Plan desinversión • Definir mercado | 4 |
| Societario | LSC Art. 160(f), 511 | España | BOE 2010 LSC | Nulidad operación | Media | Alto | • Mayorías reforzadas • Protocolos junta • Informe activo esencial | 4 |
| Protección datos | GDPR Arts. 6, 32, 35 | UE | CELEX 32016R0679 | Multa 4 % turnover | Media | Medio | • DPIA • Minimización • Cifrado | 5 |
| Ciberseguridad | NIS2 Arts. 21–23 | UE | CELEX 32022L2555 | Paro TI, sinergias −10 % | Alta | Alto | • SOC integrado • DRP • Monitorización 24/7 | 4 |
| Propiedad intelectual | TRLPI + Dir. 2009/24/CE | ES/UE | BOE TRLPI | Pérdida activos clave | Media | Medio | • Auditoría PI • Revisión contratos • Pactos transferencia | 3 |

---

### 3. Escenarios O/R/P
- **Optimista (O):** CNMC aprueba en 6m, sinergias +12 %, ROI +15 %.  
- **Realista (R):** CNMC aprueba en 12m, ajustes PI, ROI +7 %.  
- **Pesimista (P):** Bloqueo CNMC, litigios PI, ROI negativo −15 %.  

---

### 4. Simulaciones de Sensibilidad
Supuestos clave:  
- Tasa descuento __% ; sinergias netas __% ; horizonte __ meses.  

Sensibilidad:  
- **Valoración ±10 % → ΔNPV: [__, __]**  
- **Retraso regulatorio +6/+12m → ΔNPV: [__, __]**  
- **Tipos +150 pb → ΔNPV: [__, __]**  

---

### 5. Checklist Ético-Legal (10 ítems)
1. GDPR DPIA menores ✅  
2. LDC notificación CNMC ✅  
3. LSC aprobación junta ✅  
4. NIS2 plan ciberseguridad ✅  
5. PI auditoría software ✅  
6. Protocolos integridad contratos ✅  
7. Supervisión sesgos IA ⚠️  
8. Documentación ESG ⚠️  
9. Transparencia reporting ✅  
10. Confidencialidad acuerdos ✅  

---

### 6. Metadatos y QA
- Fuentes: CNMC, BOE, EUR-Lex, EDPB, ENISA.  
- Contradicciones: CNMC precedentes vs jurisprudencia TJUE.  
- “No disponible” aplicado en métricas ESG específicas.  
- Confianza media global: 4/5.  
- Fecha revisión: 2025-10-01.  

---

## ⚠️ Problemas del Nivel 5
- Requiere acceso a **datos en tiempo real** para ser efectivo.  
- La calidad depende de la actualización de fuentes oficiales.  
- Puede generar sobrecarga informativa si no se filtra bien por audiencia.  

## 🆙 Por qué N5 > N4
- N4 era un plan estratégico estático.  
- N5 añade **dashboard dinámico + simulaciones financieras + auditoría completa de fuentes**.  
- Ofrece un **sistema vivo de soporte a decisiones**, no un informe.  

## 🔎 Observaciones
El N5 en LegalTech es el **punto máximo de madurez en prompting aplicado a consultoría legal**:  
Transforma el análisis estático en un **sistema experto auditable, transparente y ético**.  
Permite al Consejo de Administración simular escenarios, cuantificar impactos financieros y revisar la trazabilidad de cada claim con confianza.  
Su fortaleza está en la **ejecutividad en tiempo real**; su desafío, en la **disponibilidad y actualización de fuentes fiables**.  

