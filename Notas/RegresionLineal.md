# Regresion Lineal Simple

### Formalizando - Analisis de regresion

Objetivos:

- Describir la relacion funcional entre X y Y

- Determinar cuanta de la variacion en Y puede ser explicada por la variacion de X y cuanto permanece sin explicar

- Predecir nuevos valores de Y para valores especificos de X en el dominio estudiado

- Relacion funcional: Puede ser de cualquier tipo.
  En RLS -> lineal

## funcion lineal

$$
Y = m*X+b
$$

- b y m son los parametros del modelo
- m = pendiente de la recta (mide el cambio en Y por cada unidad de cambio en X)
- b = ordenada al origen ("intercept") (el punto donde la recta intercepta al eje Y)

Modelo de regresion Lineal Simple (RLS)

$$
Y_i = \beta_0 + \beta_1 * x_i + \epsilon_i
$$

- $$
  $$

- $$
  $$

- $\beta_0$ y $\beta_1$ son **parametros** del modelo: ordenada al origen y pendiente

- $$

## Metodo de minimos cuadrados

- **Residuo**: es la diferencia entre el valor observado (yi) y el rpedicho por la recta propuesta x\*m + b

- La mejor recta sera la que minimice la suma de los residuos al cuadrado

  $$
  g(a,b) = \sum_{i=1}^{n}(Y_i - (b+m*X_i))^2
  $$

  - Al ser una funcion cuadratica de los parametros, tiene un minimo global que ademas es el unico minimo local

  - Lo podemos hallar buscando donde se anula el gradiente -> $\nabla(m,b) = 0$

## Prediccion

## Varianza del modelo

Cuantificando la varianza

- La variabilidad TOTAL del modelo puede separarse en EXPLICADA y NO EXPLICADA

  - Variabilidad total: $\sum_{i=1}^{n}(Y_i - Y)^2$

  - Variabilidad no explicada: $\sum_{i=1}^{n}(Y_i - \hat{Y}_i)^2$

  - Variabilidad explicada: $\sum_{i=1}^{n}(\hat{Y}_i - Y)^2$

- Coeficiente de determinacion (R^2): Mide la proporcion de variabilidad de la variable respuesta explicada por variaciones en x, es decir por el modelo de regresion

  $$
  R^2 = \frac{SCexplic}{SCtotal}
  $$

  - es una medida de la capacidad predictiva del modelo (RLS)

  - mide la "proporcion de la variabilidad en Y explicada por el modelo" (RLS)

  - es una medida de la capacidad predictiva del modelo (RLS)

  - No depende de las unidaddes de medicion

  - Toma valores entre 0 y 1

  - A mayor R^2: mas cercanos puntos a la recta

  - A mayor R^2: mayor fuerza para predecir (dentro del rango)
