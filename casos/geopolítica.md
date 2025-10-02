# Geopolítica — Caso de Prompting Especializado (Nivel 1 descriptivo)

**Objetivo:** Analizar cómo los eventos geopolíticos afectan decisiones de negocio y operaciones (suministro, compliance, precios, riesgo).  
**Rol del analista:** Consultor de geopolítica aplicado a empresa.

## 🧩 Contexto mínimo
- Región/país foco
- Sector impactado
- Horizonte temporal (corto/medio/largo)
- Interdependencias (energía, rutas, tecnología, alianzas)

## 🧠 Prompt base (descriptivo)
Eres un **Analista de Geopolítica para Negocio**. Con lenguaje claro y sin jerga innecesaria:
1) Resume el **evento geopolítico** relevante (qué, quién, cuándo, por qué).
2) Expón **impactos por dimensión**: suministro, demanda, regulación, financiero, reputacional, ciber.
3) Señala **riesgos y oportunidades** por horizonte (0–3, 3–12, 12–36 meses).
4) Propón **3 acciones de bajo coste** y **3 de alto impacto** priorizadas.
5) Incluye **KPIs (*Key Performance Indicators – Indicadores Clave de Desempeño*)** de seguimiento.

> Recuerda explicar cualquier sigla la primera vez que aparezca. Ej.: **FTA (*Free Trade Agreement – Acuerdo de Libre Comercio*)**, **WTO (*World Trade Organization – Organización Mundial del Comercio*)**, **FDI (*Foreign Direct Investment – Inversión Extranjera Directa*)**.

## 📥 Inputs sugeridos
- País/región, sector, evento clave, dependencias (energía/datos/insumos), horizonte y tolerancia al riesgo.

## 📤 Salidas esperadas
- Resumen ejecutivo (150–200 palabras)
- Mapa de impactos por dimensión
- Acciones priorizadas (quick wins / estratégicas)
- Lista de KPIs y cadencia de revisión

## ⚠️ Problemas frecuentes (y cómo mitigarlos)
```text
1) Ambigüedad del evento → Aclara fecha, actores, decisiones previstas.
2) Generalidades vacías → Forzar cuantificación (rango %, plazos).
3) Sesgo único de fuente → Triangula perspectivas (económica, seguridad, regulatoria).
4) Siglas sin expansión → Añade expansión bilingüe la primera vez.
5) Falta de priorización → Usa MoSCoW (Must/Should/Could/Won’t).

KPIs recomendados

Lead time de abastecimiento crítico (días)

% de proveedores en zonas de riesgo

Exposición a Sanciones y Controles de Exportación (EC – Export Controls)

Variación de coste logístico por ruta/puerto

MTTR (Mean Time to Recovery – Tiempo Medio de Recuperación) estimado ante disrupción

🧪 Ejemplo breve

Evento: Restricciones tecnológicas entre bloques A y B.
Impacto: Riesgo de controles de exportación en semiconductores; retrasos en certificaciones.
Acciones: (1) Alternativa de proveedor Tier-2, (2) Stock crítico 30 días, (3) Evaluar friend-shoring.
KPIs: % BOM crítico con doble sourcing, días de cobertura de inventario, coste de aranceles potenciales.
