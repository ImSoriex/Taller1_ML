# Taller 1 — Machine Learning (USFQ)

Este repositorio contiene el desarrollo completo del **Taller 1 de Aprendizaje Automático**.  
El objetivo principal es implementar y analizar dos modelos clásicos de **GLMs**:

1. **Regresión Lineal (GLM Gaussiano)** sobre el dataset **Boston Housing**:
   - Predicción del precio medio de las viviendas (`MEDV`).
   - Muestreo reproducible (`random_state=XXXX`).
   - Análisis exploratorio (EDA), correlaciones, histogramas y gráficos de dispersión.
   - Ajuste del modelo lineal múltiple.
   - Interpretación de coeficientes significativos.
   - Evaluación: R², R² ajustado, supuestos (normalidad, homocedasticidad, multicolinealidad).

2. **Regresión Logística (GLM Bernoulli)** sobre el dataset **Breast Cancer Wisconsin**:
   - Clasificación de tumores: 0 = Benigno, 1 = Maligno.
   - Muestreo reproducible de 400 observaciones.
   - Análisis exploratorio: distribución de clases, variables clave.
   - Preprocesamiento: estandarización, train/test split estratificado.
   - Ajuste del modelo logístico.
   - Interpretación de coeficientes mediante *Odds Ratios*.
   - Evaluación: Accuracy, Recall, F1-score y Matriz de Confusión.

## ⚙️ Reproducibilidad

- La semilla de muestreo se fija con los **últimos 4 dígitos de cédula** (`random_state=XXXX`), garantizando reproducibilidad.
- Todos los experimentos se realizaron en **Python 3.10+** con librerías estándar:
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `scikit-learn`
  - `statsmodels`
## 🚀 Cómo correr los notebooks

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ImSoriex/Taller1_ML
   cd Taller1_ML
2. Crear entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
# Autor
**Emilio Soria**

Estudiante de Ing. en Ciencias de la Computación.

## 📜 Licencia
Este proyecto es de uso académico. Puedes usar el código como referencia, 
pero no está destinado a uso comercial.
