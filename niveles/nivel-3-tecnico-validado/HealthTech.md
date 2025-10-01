# Nivel 3 — Técnico Validado (HealthTech)

## Rol
Actúa como **consultor regulatorio sanitario especializado en dispositivos médicos de IA**.

## Caso
Hospital de Madrid implementa un sistema de **IA radiológica diagnóstica**.

## Contexto
Normativa: **MDR (2017/745 UE)**, **GDPR art. 9**, **NIS2**.

## Instrucciones
1. Identifica 5 riesgos principales (certificación CE, GDPR, sesgo clínico, ciberseguridad hospitalaria, interoperabilidad).  
2. Estima impacto (€ y KPIs clínicos).  
3. Escenarios (optimista, realista, crítico).  
4. Tabla Top-5 riesgos.  
5. Checklist: certificación CE, DPIA, ciberseguridad, formación, *human-in-the-loop*.

## Tabla Top-5 Riesgos
| # | Riesgo | Norma/Art. | Impacto | Prob. | Mitigación | Confianza |
|---|--------|------------|---------|-------|------------|-----------|
| 1 | Certificación CE retrasada | MDR Arts. 52–54 | Retraso ≥12m, coste +1 M€ | Media | • Pre-consulta autoridad • Ensayos multicéntricos • Documentación robusta | 4/5 |
| 2 | GDPR (datos clínicos sensibles) | GDPR Art. 9, 32 | Multa hasta 4 % turnover; pérdida confianza | Media | • DPIA • Anonimización • Seguridad reforzada | 5/5 |
| 3 | Sesgo clínico IA | MDR + Ética IA UE 2019 | Falsos positivos/negativos; riesgo legal | Baja-Media | • Dataset diverso • Auditoría continua • Human-in-loop | 4/5 |
| 4 | Ciberseguridad hospitalaria | NIS2 Arts. 21–23 | Paro sistema 48h; impacto clínico severo | Media-Alta | • SOC hospitalario • Backups cifrados • Plan contingencia | 4/5 |
| 5 | Interoperabilidad limitada | HL7/FHIR + MDR | Costes ocultos integración +20% | Media | • Test integraciones • APIs estandarizadas • Vendor neutral | 3/5 |

## Supuestos y Sensibilidad
- Reducción tiempo informe __%  
- Coste certificación CE __M€  
- Horizonte __ meses  
- Especificidad −3pp → Δcoste relecturas [__, __]  
- Ciberincidente 48h → Δimpacto clínico [__, __]  
- Integración +20% → ΔNPV [__, __]

## Problemas del Nivel 3
- Costes ocultos subestimados.  
- Validación parcial si no es *multi-site*.  
- Falta plan clínico asistencial a 5 años.

## Por qué N4 es mejor
- Añade benchmark hospitales UE.  
- PESTEL/ESG + roadmap clínico.  
- KPIs de impacto sanitario y sostenibilidad.

## Observaciones
El N3 en HealthTech es útil para **comités médicos y de innovación hospitalaria**: permite evaluar si la tecnología es viable en el corto plazo y qué riesgos inmediatos pueden surgir.  
Ofrece una visión clara sobre certificación, privacidad y ciberseguridad, pero aún no aborda **modelos de escalabilidad internacional, impacto social ni sostenibilidad financiera**.  
Tampoco incorpora comparativas entre hospitales o países, ni alinea la tecnología con **estrategias sanitarias nacionales o europeas**.  
Es un **diagnóstico inicial muy valioso**, pero necesita evolucionar hacia N4 para convertirse en un **plan estratégico de adopción clínica a gran escala**.
