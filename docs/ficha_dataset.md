# Ficha del dataset — Ejercicio 01

## Pregunta y contexto
- **Dominio:** Riesgo crediticio (finanzas)
- **Unidad de análisis:** Cada fila representa una solicitud de crédito individual.
- **Decisión que apoya el modelo:** Determinar si un banco debería aprobar o rechazar una solicitud de crédito según el riesgo estimado.
- **Target tentativo:** Clasificación del riesgo crediticio (bueno / malo).
- **Tipo de tarea:** Clasificación binaria.
- **Error más costoso:** Clasificar como "buen riesgo" a alguien que en realidad es "mal riesgo" (falso negativo) — el banco pierde dinero al otorgar un crédito que no se pagará. El propio dataset incluye una matriz de costos que confirma esto: es 5 veces más costoso este error que el opuesto.
- **Usuario de la solución:** Analista de riesgo crediticio de una institución financiera.

## Comparación de candidatos

| Criterio | Candidato A: German Credit | Candidato B: Predict Students Dropout |
|---|---|---|
| Procedencia | UCI Machine Learning Repository (Prof. Hans Hofmann, 1994) | UCI Machine Learning Repository (Realinho et al., 2021) |
| URL ficha | https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data | https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success |
| Licencia | CC BY 4.0 | CC BY 4.0 |
| Filas / columnas | 1,000 filas / 20 variables | 4,424 filas / 36 variables |
| Target y clases | Binario: buen riesgo / mal riesgo | 3 clases: Dropout / Enrolled / Graduate (se reduciría a binario) |
| Ausentes | Sin valores ausentes reportados | Sin valores ausentes reportados |
| Riesgo de fuga | Bajo — variables conocidas al momento de la solicitud | Medio — hay que verificar que ninguna variable de rendimiento del 2do semestre se use si el objetivo es predicción temprana |

## Decisión propuesta
Se propone trabajar con el **Candidato A (German Credit)** por:
1. Ser binario desde el origen (sin necesidad de decisiones adicionales sobre reducción de clases).
2. Tamaño más manejable para múltiples repeticiones de entrenamiento (requerido en LAB03/Ejercicio 02).
3. Contar con una matriz de costos ya definida por los autores, que refuerza el análisis de qué error es más costoso.
