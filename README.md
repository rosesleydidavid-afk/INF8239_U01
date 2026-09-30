# INF8239_U01 — Ejercicio 01: SVM y Dataset Público (German Credit)

## Objetivo
Construir un pipeline de clasificación reproducible y sin fuga de datos, primero validando el procedimiento con un dataset de práctica (Breast Cancer, LAB01), y luego aplicándolo a un dataset real de riesgo crediticio (German Credit, LAB02), comparando una línea base contra un modelo SVM optimizado.

## Problema
Determinar si un solicitante de crédito representa un buen o mal riesgo crediticio, a partir de 20 variables disponibles al momento de la solicitud (historial crediticio, monto solicitado, situación laboral, entre otras).

## Fuente de datos
- **Dataset:** Statlog (German Credit Data)
- **Origen:** UCI Machine Learning Repository, donado por el Prof. Hans Hofmann (1994)
- **Licencia:** CC BY 4.0
- **URL:** https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data
- **Descarga:** vía paquete oficial `ucimlrepo` (encapsulado en `src/inf8239_u01/data.py`), ya que el dataset no se distribuye como CSV plano.

## Instalación y ejecución

### 1. Clonar el repositorio y crear el entorno virtual
```
git clone https://github.com/rosesleydidavid-afk/INF8239_U01.git
cd INF8239_U01
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Ejecutar los notebooks en orden
1. `notebooks/00_verificacion.ipynb` — valida el entorno.
2. `notebooks/01_svm_guiada.ipynb` — SVM guiada sobre dataset de práctica (Breast Cancer).
3. `notebooks/02_dataset_publico.ipynb` — descarga, auditoría y SVM sobre German Credit.

### 3. Ejecutar las pruebas
```
$env:PYTHONPATH="src"
python -m pytest -q
```
Resultado esperado: `10 passed`.

## Métrica principal y clase prioritaria
- **Métrica:** F1 macro (adecuada por el desbalance de clases 70/30).
- **Clase prioritaria:** "Mal riesgo" (clase 2) — según la matriz de costos oficial del dataset, un falso negativo (aprobar a un mal pagador) cuesta 5 veces más que un falso positivo (rechazar a un buen pagador).

## Resultados principales

| Modelo | Dataset | F1 macro | Recall clase minoritaria |
|---|---|---|---|
| Dummy (baseline) | Breast Cancer | 0.387 | — |
| SVM (C=10, gamma=0.01) | Breast Cancer | 0.981 | — |
| Dummy (baseline) | German Credit | 0.412 | — |
| SVM (C=1, gamma="scale", sin balancear) | German Credit | 0.720 | 0.48 |
| **SVM (C=1, gamma="scale", class_weight="balanced")** | **German Credit** | **0.736** | **0.77** |

## Estructura del repositorio
```
INF8239_U01/
├── docs/
│   ├── ficha_dataset.md
│   └── diccionario_datos.md
├── notebooks/
│   ├── 00_verificacion.ipynb
│   ├── 01_svm_guiada.ipynb
│   └── 02_dataset_publico.ipynb
├── src/inf8239_u01/
│   ├── environment.py
│   ├── models.py
│   ├── data.py
│   └── credit_models.py
├── tests/
│   ├── test_environment.py
│   ├── test_models.py
│   ├── test_credit_models.py
│   └── test_data_contract.py
├── reports/
│   ├── svm_cv_results.csv
│   ├── credit_cv_results.csv
│   └── (modelos .joblib, no versionados)
├── requirements.txt
└── .gitignore
```

## Limitaciones
- El dataset tiene solo 1,000 filas — un tamaño modesto que limita la robustez de la validación cruzada (desviaciones estándar de hasta 0.04 entre pliegues).
- Las variables categóricas provienen de codificaciones alemanas de los años 90 (montos en Marcos Alemanes, categorías laborales de esa época) — su vigencia para un contexto crediticio actual es limitada.
- No se realizó calibración de probabilidades pese a usar `probability=True`; si se necesitaran probabilidades confiables para fijar un umbral de decisión, correspondería aplicar `CalibratedClassifierCV` en un trabajo futuro.

## Ejercicio 02 — Ensambles, reducción dimensional y Green AI

### Modelos comparados
Se evaluaron 6 configuraciones bajo el mismo protocolo (partición, métrica F1 macro): regresión logística, SVM (C=1 y C=10, ambas con `class_weight="balanced"`), Random Forest (100 y 300 árboles, balanceado) y HistGradientBoosting.

### Resultados principales

| Modelo | F1 macro | Tiempo ajuste (mediana) | Tamaño | Pareto |
|---|---|---|---|---|
| **svm_c1** | **0.736** | 1.38s | 305 KB | ✅ |
| **logistic** | **0.721** | **0.25s** | **7.9 KB** | ✅ |
| svm_c10 | 0.727 | 1.99s | 281 KB | ❌ |
| rf_300 | 0.697 | 3.17s | 3,864 KB | ❌ |
| boost | 0.688 | 1.77s | 210 KB | ❌ |
| rf_100 | 0.675 | 1.20s | 1,316 KB | ❌ |

### Reducción dimensional
- **PCA**: redujo de 61 a 32 dimensiones (95% de varianza), con una caída de F1 macro de 0.736 a 0.712.
- **t-SNE** (dos semillas, 42 y 7): estructura razonablemente estable entre semillas, pero sin separación visual clara entre clases — coherente con la dificultad del problema.

### Decisión Pareto
Solo `svm_c1` y `logistic` quedan en la frontera de Pareto. Se selecciona **svm_c1** como modelo final: aunque `logistic` es 81.9% más rápida y 38.6 veces más liviana, `svm_c1` ofrece 5.2 puntos porcentuales más de recall — crítico dado que la matriz de costos oficial del dataset penaliza los falsos negativos 5 veces más que los falsos positivos.

### Entorno de medición
Python 3.14.2, Windows 11, Intel64 Family 6 Model 122, scikit-learn 1.9.1. Los tiempos reportados son específicos de este hardware y no deben interpretarse como valores absolutos.