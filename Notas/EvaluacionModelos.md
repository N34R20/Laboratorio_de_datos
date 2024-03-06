# Evaluacion

Metodologia de evaluacion

Objetivos:

- Comparar dos modelos

- Estimar la performance

Es fácil errar en la creación de un modelo (entrenamiento), pero también es fácil darse cuenta.

Es fácil errar en la evaluación y no es fácil darse cuenta.

Evaluar bien significa entender bien el caso de uso, entender qué me importa del problema y qué no, entender qué métrica/s refleja/n lo que quiero capturar, entender qué mecanismo de evaluación usar, entender cómo no hacer/se trampa como hago que no me hagan trampa

## Cross Validation (Validacion Cruzada)

Porque no medimos sobre los datos de entrenamiento?

1. Separo una porcion de los datos que NO voy a usar para entrenar!

2. Mido la performance del modelo sobre los datos de validacion (en general suelen ser el 5%, 10%, 20% del total de datos)

-> esta tecnica suele ser suficiente si tengo muchos datos

```python
sklearn.model_selection.train_test_split()
```

## K-Fold Cross Validation

Y si tenemos mala suerte al separar los datos para entrenamiento/validacion?

- La estimacion de performance del modelo podria no ser realista. En especial cuando tenemos pocos datos!

La idea es generar distintas particiones para armar k datasets distintos a partir de mi dataset original.

Ej: evaluando un modelo particular con sus hiper-parámetros. Por ejemplo, un árbol de decisión con altura 10 o un modelo de KNN con k = 3

Input:
L (un algoritmo de aprendizaje + sus
hiperparametros) D el “dataset’

1. Separamos D en K subconjuntos a los que llamamos folds: D1 , D2 , D3 , …, DK

2. Construimos K modelos con el algoritmo y hiperparametros de L que serán entrenados utilizando todos los datos salvo los del k-ésimo fold.

3. Para cada x(i) ∈ D:
   pred(i) = modelo_que_no_vio_ese_dato_en entrenamiento.predict()
   predicciones[i] = pred(i) # juntamos las predicciones como si vinieran todas del mismo modelo

4. Computamos alguna métrica del error(\*\*) sobre el conjunto entero predicciones vs y

## Busqueda del mejor modelo

Para poder elegir un modelo final, es natural explorar distintas combinaciones de hiper-parámetros y distintos algoritmos de aprendizaje

## Seleccion de Modelos

## Proceso de seleccion de modelos

- 1. Separo los datos en DEV y EVAL

- 2. Con los datos en DEV

  - a) Armo una grilla con lso hiperparametros a explotar para cada modelo

  - b) Evaluar cada configuracion con cross-validation

  - c) Tomo como modelo final

- 3. Con los datos EVAL

  - a) Calculo la performance del modelo

# Metricas de performance

Regresion:

$$
MSE = \frac{1}{n}\sum_{i=1}^n(Y_i-\hat{Y}_i)^2
$$

Clasificacion:

$$
Accuarcy = \frac{InstanciasBienCalificadas}{TotalDeInstancias}
$$

¿Qué significa si me dicen: Mi modelo tiene accuracy del 80%?
→ De 100 muestras 80 las clasificó bien

No dice nada sobre el tipo de aciertos y errores que comete el modelo

Tipos de error

- **Falso Positivo**: Era negativo pero dijimos positivo

- **Falso Negativo**: Era positivo pero dijimos negativo

Matriz de confusion

$$

\begin{bmatrix}
\text{TN} & \text{FP} \\
\text{FN} & \text{TP}
\end{bmatrix}


$$

#### Accuracy

$$
Accuarcy = \frac{TP + TN }{TP + TN + FP + FN}
$$

#### Precision

$$
Precision = \frac{TP}{TP + FP}
$$

De las instancias clasificadas como positivas, cuantas lo son (cuan utiles son los resultados de busqueda)

#### Recall

$$
Recall = \frac{TP}{TP + FN}
$$

De las instancias positivas, cuantas fueron clasificadads como positivas (cuan completos son los resultados)

#### Caso bianrio : F-score

$$
F_{\beta} = (1 + \beta^2) * \frac{precision * recall}{(\beta^2 * precision) + recall}
$$

#### Curvas ROC

Grafico Recall vs False Positive Recall
