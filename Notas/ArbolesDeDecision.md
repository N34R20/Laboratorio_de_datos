# Arboles de Decision

Se basa en el armado de una **jerarquia de reglas**, que pueden ser expresadas usando formulas logicas ANDs y ORs.

El arbol representa una **disyuncion de conjunciones sobre valores de atributos**.

(Sex == Female) ^ (Age < 5) V (Age >= 5 ^ Pclass == 1)

- Los arboles son altamente interpretables -> dada una prediccion particular podemos entender porque la genero.

**Input**: S un conjunto de instancias con atributos A.

1. Elegimos a ∊ A, el atributo que produce el “mejor corte” de S para el nodo_actual

2. Para cada valor v i posible de a, crear un nuevo hijo del nodo_actual

3. Clasificar (repartir) las instancias en los nuevos nodos, según el valor de a.
   S i ← { x | x ∊ S ∧ x[a] = v i }

4. Si las instancias están bien clasificadas o se cumple algún criterio de corte: TERMINAR
   Si no: Iterar sobre los hijos del nodo actual con A i ← A - {a}.

   ¿Cómo definimos el mejor corte?

   → Necesitamos métricas!!

## Medidas de impureza

$$
\Delta M(S,c) = M(S) - (Prop_{c,<=} * M(Prop_{c,<=}) + Prop_{c,>} * M(S_{c,>}))
$$

**“cuánto gano si divido a S en regiones S c, <=y S c, > según la medida M.“ (caso binario)**

### Entropia

mide el nivel promedio de "Informacion", "sorpresa" o "incertidumbre" inherente a los posibles resultados de una variable aleatoria.

$$
H(S) = - \sum_{k \in clases(S)} p_s (k) = \Epsilon[-log(p_s(k))]
$$

### Info Gain (Ganancia de informacion)

cuanta entropia removemos al hacer un corte.

$$
InfoGain(S, <a,c>) = H(S) - (Prop_{<=} * H(S_{<=}) + Prop_> * H(S_>))
$$

### Gini Gain

La impureza de Gini mide la probabilidad de que una instancia particular sea clasificada erroneamente, si esta fuese etiquetada aleatoriamente de acuerdo con la distribucion de clases dentro de la region

$$
Gini(S) = 1 - \sum_{k \in clases(K)} (p_s (k))^2
$$

$$
Gini Gain(S, <a,c>) = Gini(S) - (Prop_{<=} * Gini(S_{<=}) + Prop_> * Gini(S_>))
$$

## Sesgo Inductivo

Conjunto de supuestos y conocimientos previos que el algoritmo de aprendizaje utiliza para hacer
predicciones sobre nuevos datos no vistos, basándose en los datos de entrenamiento que ha visto.
Estos supuestos pueden provenir de una variedad de fuentes, incluyendo:

➔ Estructura del modelo

➔ La función objetivo que el algoritmo esté optimizando

➔ Características de funcionamiento del algoritmo (cómo recorre el espacio de hipótesis hasta elegir
un único modelo, la semilla utilizada)

➔ etc

El sesgo inductivo determina los tipos de funciones que el algoritmo puede aprender y los tipos de
errores que se espera que cometa

¿Cual es el sesgo inductivo de los árboles?

- Las regiones son rectangulares

- Los atributos más discriminativos están cerca de la raíz (por cómo se toma el mejor corte).

- Árboles más pequeños y menos complejos en términos de su estructura de acuerdo al criterio de
  parada establecido.

## Generalizacion

Queremos un modelo lo suficientemente rico para captar
ideas complejas. Pero sin caer en:

#### Subajuste (underfitting)

Construcción de un modelo
demasiado simple que no capture
la información disponible.

#### Sobreajuste (overfitting)

Construcción de un modelo
demasiado complejo para la
cantidad de información que
disponemos.

### Modelos Simples

Una de las formas de evitar el sobreajuste es simplificar los modelos. En general queremos que nuestros modelos cumplan:

Cuando tenemos dos modelos que compiten y producen las mismas predicciones, debemos elegir el más simple. Un modelo más simple es aquel que tiene menos parámetros o menor complejidad estructural.

¿Por qué? En la práctica se ve que ayuda a:

➔ Evitar el sobreajuste y por lo tanto mejorar el
rendimiento en datos no vistos.

➔ Mejora la interpretación. Los modelos más
simples son más fáciles de interpretar y entender.

➔ Reduce los costos computacionales.

En el caso de los árboles, ¿cuál es
el menos complejo?

Navaja de Ockham (un principio metodológico y filosófico).
