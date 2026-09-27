# Diccionario de datos — German Credit Data

| Columna | Nombre real | Tipo | Significado | Momento de disponibilidad |
|---|---|---|---|---|
| Attribute1 | Estado de cuenta corriente | Categórica | Saldo de la cuenta corriente (en Marcos alemanes): <0, 0-200, ≥200, o sin cuenta | Al momento de la solicitud |
| Attribute2 | Duración | Numérica | Duración del crédito solicitado, en meses | Al momento de la solicitud |
| Attribute3 | Historial crediticio | Categórica | Si pagó créditos anteriores a tiempo, con atrasos, o cuenta crítica | Al momento de la solicitud |
| Attribute4 | Propósito | Categórica | Para qué es el crédito: auto nuevo/usado, muebles, TV, educación, negocio, etc. | Al momento de la solicitud |
| Attribute5 | Monto del crédito | Numérica | Cantidad solicitada | Al momento de la solicitud |
| Attribute6 | Cuenta de ahorros | Categórica | Saldo en cuenta de ahorros/bonos | Al momento de la solicitud |
| Attribute7 | Antigüedad laboral | Categórica | Años en el empleo actual | Al momento de la solicitud |
| Attribute8 | Tasa de cuota | Numérica | Cuota del crédito como % del ingreso disponible | Al momento de la solicitud |
| Attribute9 | Estado civil y sexo | Categórica | Combinación de estado civil y sexo del solicitante | Al momento de la solicitud |
| Attribute10 | Otros deudores/garantes | Categórica | Si tiene co-solicitante o garante | Al momento de la solicitud |
| Attribute11 | Residencia actual | Numérica | Años en la residencia actual | Al momento de la solicitud |
| Attribute12 | Propiedad | Categórica | Tipo de propiedad más valiosa que posee | Al momento de la solicitud |
| Attribute13 | Edad | Numérica | Edad en años | Al momento de la solicitud |
| Attribute14 | Otros planes de pago | Categórica | Si tiene otros créditos con bancos o tiendas | Al momento de la solicitud |
| Attribute15 | Vivienda | Categórica | Renta, propia, o gratuita | Al momento de la solicitud |
| Attribute16 | Créditos existentes | Numérica | Cantidad de créditos actuales en este banco | Al momento de la solicitud |
| Attribute17 | Empleo/ocupación | Categórica | Nivel de cualificación laboral | Al momento de la solicitud |
| Attribute18 | Personas a cargo | Numérica | Cantidad de personas que dependen económicamente del solicitante | Al momento de la solicitud |
| Attribute19 | Teléfono | Categórica | Si tiene teléfono registrado a su nombre | Al momento de la solicitud |
| Attribute20 | Trabajador extranjero | Categórica | Si es trabajador extranjero (sí/no) | Al momento de la solicitud |
| class | **Target** | Numérica (1/2) | 1 = buen riesgo crediticio, 2 = mal riesgo crediticio | Se conoce DESPUÉS de otorgado el crédito — nunca debe usarse como predictor |

## Nota sobre riesgo de fuga
**Todas las variables Attribute1-Attribute20 están disponibles al momento de la solicitud del crédito** — es decir, son información que el banco ya tiene ANTES de decidir si aprueba o no. Ninguna depende de eventos posteriores a la decisión, por lo que no representan riesgo de fuga temporal (conectando con el principio de U01.01: separar momento de observación, momento de decisión y momento del resultado).

## Matriz de costos oficial del dataset
El propio dataset (Hofmann, 1994) incluye una matriz de costos que cuantifica el error más costoso:

|  | Predicho: Bueno | Predicho: Malo |
|---|---|---|
| **Real: Bueno** | 0 | 1 |
| **Real: Malo** | 5 | 0 |

Es decir: clasificar a un mal pagador como "buen riesgo" (falso negativo) es **5 veces más costoso** que clasificar a un buen pagador como "mal riesgo" (falso positivo). Esto confirma cuantitativamente la decisión metodológica documentada en la ficha del dataset.

## Fuentes
- UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data
- Documentación técnica original (Prof. Hans Hofmann, Universität Hamburg)