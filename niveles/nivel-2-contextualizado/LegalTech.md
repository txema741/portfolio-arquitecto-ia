# Nivel 2 — Contextualizado (Legal-Tech)

## 📖 Descripción
En el **Nivel 2**, el prompting se enriquece con **rol, escenario y contexto**.  
El objetivo es simular la respuesta de un **experto legal en un caso concreto**, reduciendo la vaguedad del Nivel 1 y acercándose a una salida con valor práctico.

---

## 📝 Prompt
Actúa como un **abogado senior especializado en fusiones y adquisiciones en España**.  
Escenario: revisión de una fusión entre dos empresas de software valorada en 150 millones de euros.  
Contexto: la operación involucra jurisdicción española y normativa europea (**Directiva de Fusiones de la UE 2004/25/CE**).  
Instrucción: identifica los **5 principales riesgos legales** con:  

- Referencias a artículos concretos de la **Ley de Sociedades de Capital** y la **Ley de Defensa de la Competencia**.  
- Impacto potencial en la operación.  
- Recomendaciones básicas de mitigación.  

**Objetivo:** preparar un briefing para el consejo de administración.

---

## 📤 Salida esperada (ejemplo de IA)
1. **Riesgo de competencia (art. 2, Ley de Defensa de la Competencia):**  
   La fusión puede generar abuso de posición dominante.  
   - *Impacto:* retraso en aprobación, sanciones de hasta el 10% del volumen de negocio.  
   - *Mitigación:* notificar preventivamente a la CNMC, presentar plan de desinversión parcial.  

2. **Riesgos societarios (arts. 160 y 511 Ley de Sociedades de Capital):**  
   Falta de aprobación en junta de accionistas o conflictos de gobierno corporativo.  
   - *Impacto:* nulidad de la operación.  
   - *Mitigación:* preparar votación anticipada, asegurar mayorías reforzadas.  

3. **Propiedad intelectual:**  
   Disputas sobre licencias de software y patentes no transferibles.  
   - *Impacto:* pérdida de activos clave, litigios internacionales.  
   - *Mitigación:* auditoría de licencias antes del cierre.  

4. **Contratos laborales y de proveedores:**  
   Riesgo de incumplimiento por incompatibilidad de acuerdos vigentes.  
   - *Impacto:* reclamaciones económicas, pérdida de clientes clave.  
   - *Mitigación:* renegociación previa de contratos sensibles.  

5. **Riesgo regulatorio europeo (Directiva de Fusiones UE 2004/25/CE):**  
   Posible obligación de notificación transfronteriza si la operación afecta a varios países.  
   - *Impacto:* plazos de revisión más largos.  
   - *Mitigación:* incluir calendario realista y cláusulas suspensivas.  

---

## ⚠️ Problemas del Nivel 2
1. Aunque más detallada, la salida puede quedarse corta en *jurisprudencia y precedentes*.  
2. No incluye análisis económico cuantitativo (proyecciones de pérdidas si no se mitiga).  
3. Puede omitir normativas secundarias (protección de datos, ciberseguridad).  
4. El formato de "lista de riesgos" sigue siendo útil, pero no equivalente a un informe jurídico real.  

---

## 🔎 Observaciones
El **Nivel 2 — Contextualizado** ya proporciona un **briefing útil para directivos**, con referencias legales y mitigaciones claras.  
Sin embargo, aún no alcanza la robustez de un análisis profesional completo.  

👉 El salto al **Nivel 3 — Analítico** se enfocará en integrar **jurisprudencia, métricas cuantitativas y escenarios comparativos**.
