# Nivel 2 — Contextualizado (FinTech)

## 📖 Descripción
En el **Nivel 2**, el prompting se enriquece con **rol, escenario y contexto**.  
El objetivo es simular la respuesta de un **experto financiero en un caso concreto**, reduciendo la vaguedad del Nivel 1 y acercándose a una salida con valor práctico.

---

## 📝 Prompt
Actúa como un **consultor senior en regulación financiera especializado en FinTech y pagos digitales en la Unión Europea**.  
Escenario: una startup española quiere lanzar una **plataforma de pagos transfronterizos** basada en blockchain para operar en toda la UE.  
Contexto: la operación debe cumplir con el **Reglamento MiCA (Markets in Crypto-Assets – Mercados de Criptoactivos)**, la **PSD2 (Payment Services Directive 2 – Directiva de Servicios de Pago 2)** y la normativa de **prevención de blanqueo de capitales (AML – Anti Money Laundering / Prevención del Blanqueo de Capitales)**.  
Instrucción: identifica los **5 principales riesgos regulatorios y de negocio** con:  

- Referencias a normativas europeas aplicables.  
- Impacto potencial en la viabilidad del proyecto.  
- Recomendaciones básicas de mitigación.  

**Objetivo:** preparar un briefing para los fundadores antes de buscar inversión.

---

## 📤 Salida esperada (ejemplo de IA)
1. **Riesgo de autorización regulatoria (MiCA, art. 59):**  
   La plataforma requiere registro como proveedor de servicios de criptoactivos.  
   - *Impacto:* bloqueo del lanzamiento en la UE.  
   - *Mitigación:* iniciar proceso de autorización en CNMV con asesoría especializada.  

2. **Riesgo de cumplimiento en pagos (PSD2, arts. 4 y 66):**  
   Exigencia de autenticación reforzada de clientes (SCA – Strong Customer Authentication / Autenticación Reforzada de Clientes).  
   - *Impacto:* costes adicionales en seguridad e integración tecnológica.  
   - *Mitigación:* integrar APIs de open banking ya certificadas.  

3. **Prevención de blanqueo de capitales (AMLD5 – 5th Anti-Money Laundering Directive / 5ª Directiva de Blanqueo de Capitales):**  
   Riesgo de sanciones si no se aplican procedimientos KYC (Know Your Customer – Conozca a su Cliente).  
   - *Impacto:* multas y pérdida de licencia.  
   - *Mitigación:* contratar soluciones KYC externas homologadas.  

4. **Ciberseguridad (NIS2 – Network and Information Security Directive / Directiva de Seguridad de Redes y Sistemas de Información):**  
   Posibilidad de ataques sobre la red blockchain y filtración de datos.  
   - *Impacto:* pérdida de confianza de clientes e inversores.  
   - *Mitigación:* auditorías de ciberseguridad periódicas y pólizas de ciberseguro.  

5. **Riesgo de escalabilidad y liquidez:**  
   Modelo de negocio puede no sostener grandes volúmenes de transacciones en fases iniciales.  
   - *Impacto:* fallos en la operativa y fuga de clientes.  
   - *Mitigación:* estrategia de escalado progresivo y acuerdos con bancos custodios.  

---

## ⚠️ Problemas del Nivel 2
1. No incluye métricas financieras detalladas (ej. proyecciones de ingresos y costes de cumplimiento).  
2. La salida sigue centrada en riesgos regulatorios, pero no aborda estrategias de captación de clientes o competencia.  
3. No se consideran diferencias entre países de la UE (ej. España vs. Alemania en requisitos adicionales).  
4. Aunque realista, aún no equivale a un informe de due diligence completo.  

---

## 🔎 Observaciones
El **Nivel 2 — Contextualizado** en FinTech ya entrega un **briefing estratégico para fundadores e inversores**, señalando los principales riesgos regulatorios y de negocio con medidas de mitigación básicas.  

👉 El salto al **Nivel 3 — Analítico** permitirá integrar **proyecciones económicas, benchmarking competitivo y escenarios financieros comparativos**.
