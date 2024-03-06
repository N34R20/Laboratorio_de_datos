# Aprendizaje No Supervisado

Hasta ahora las observaciones tenían variables predictoras y un valor a predecir conocido (etiquetas).

No contamos datos de entrenamiento etiquetados. Se trata de descubrir información y estructura implícita en los datos sin ninguna guía externa.

Es decir, descubrir patrones o estructuras ocultas en los datos sin la presencia de etiquetas o respuestas predeﬁnidas.

Sirve para entender, resumir, relacionar y visualizar los datos.

Estrategias que veremos:

- Clustering - Agrupamiento

  - Metodos para encontrr subgrupos homogeneos dentro del conjunto entero de los datos

- Reducción de la dimensión
  Metodos para proyectar los datos (en general de dimensiones altas) en un espacio de menor dimension, que haga posible su manipulacion (o visualizacion) pero preserve las caracteristicas del conjutno original. Suele usarse tambien como paso previo al clustering.

# Clustering (agrupamiento)

Encontrar **grupos de instancias (clusters)** a partir de informacion en los datos que describan objetos y sus relaciones.

Instancias de un cluster tienen que ser:

- similares entre si y difernetes a las de otros clusters

## Algortimos de Clusetring

- **De particion:** se clasifican m datos con k clusters.
  Cada clusetr satisface requerimientos de una particion

  - cada dato esta en un y solo un cluster
  - cada cluster debe tener al menos un dato

- **Jerarquicos:**

  - **Aglomerativos (bottom up)**: empiezan con n clusters (cada datos es un clusetr) y se combinan grupos

  - **Divisorios (top down)**: comienzan con un cluster de n observaciones y en cada paso se dividen

# K-Means

optimizacion
funcion a optimizar: Funcion de **distorsion**

$$
J = \sum_{i=1}^{m} \sum_{k=1}^{K} a_{ik} * || x^{(i)} - \mu_k ||^2
$$

K-means intenta encontrar $\mu_k$ y $a_{ik}$ que minimicen J:

- En **asignacion de cluster**

- En **actualizacion de centroide**

#### Ventajas

- Rapido
- Facil de implementar
- Util en general

#### Desventajas

- Sensible a ruido y outliers
- Necesita especificar el numero de clusters de antemano
- No es bueno cuando los datos tienen formas raras, o cuadno hay mucha variabilidad en los tamaño de los clusters
- Sensibilidad a los valores inicieales de los centroides

# DBSCAN

### Density-based spatial clustering of applications with noise

Algoritmo

    Parametros:
    - Eps -> Distancia para la vecinadad
    - minPts -> Cantidad de vecinos requeridos

- Un punto p es un punto _nucleo_ si al menos minPts puntos estan a una distancia menor a Eps de el

- Un putno q es _alcanzable_ desde p si hay un camino de puntos alcanzables que va de p a q

- Un punto que no sea alcanzable desde al menos minPts es considerado _ruido_.

1. Para cada observación miramos el número de puntos a una distancia máxima Eps de ella. Esta zona se denomina Eps-vecindad de la observación.

2. Si una observación tiene al menos minPts vecinos, incluida ella misma, se considera una observación central. En este caso, se ha detectado una observación de alta densidad.

3. Todas las observaciones en la vecindad de una observación central pertenecen al mismo cluster. Puede haber observaciones centrales cercanas entre sí. Por lo tanto, de un paso a otro, se obtiene una larga secuencia de observaciones centrales que constituyen un único cluster.

4. Cualquier observación que no sea una observación central y que no tenga ninguna observación central en su vecindad se considera una anomalía/outlier.

#### Ventajas

- No asume nigun numero de clusters
- Puede encontrar clusters con formas geometricas arbitrarias
- Es robusto detectando outliers
- No es suceptible al roden en que se encuentran los putnos dentro de la abse de datos, ni a la inicializacion

#### Desventajas

- No puede agrupar bien conjutnos de datos con grandes diferencias en las densidades
- Es muy sensible a los parametros (minPts y Eps) y a veces es dificil determinarlos
- No es bueno para datasets muy grande o en muchas dimensiones.

# Clustering Jerarquico

1. Cada punto forma un cluster
2. Computar matriz de cercanía
3. Repetir:
   - a. Buscar el par de clusters más similar y hacer un merge
   - b. Actualizar la matriz de proximidad hasta que haya un solo cluster

Este proceso genera un dendograma.

## Dendograma

La altura representa la escala a la que se unen los clusters

Una vez hecho el dendograma, se lo puede cortar en una altura y asi generar el clustering

## Criterios de cercania

Entre dos putnos - la ceracnia es la distancia (que depende de los atributos).

## Medicion de similaridad entre clusters

- **Single linkage**: distancia minima entre dos putnos de los dos distintos clusters

- **Complete linkage**: distancia maxima entre dos putnos de los distintos clusters

- **Average linkage**: promedio de la distancia entre los putnos de los clusters

- **Centroid linkage**: distancia entro centroides

#### Ventajas

- No asume nigun numero de clusters (se pueden obtener cortando el dendograma en el nivel deseado)
- Genera un dendograma que puede ser util para interpretar el algoritmo

#### Desventajas

- Sensible a ruido y outliers
- Computacionalmente caro en tiempo y en espacio
- No siempre la estructura jerarquica es la mas adecuada
- Optimiza localmente, no de manera global

# Reduccion de la dimension

Objetivo:

- Visualizacion
- Interpretacion de los datos
- Regularizacion de los datos
- Simplificacion de los modelos a utilizar

### Algunas Tecnicas

- PCA: Principal Component Analysis

- MDS: Multidimensional Scaling

- ISOmap: Isometric Feature Mapping

- t-SNE: t-Stochastic Neighbor Embedding

## PCA - Principal Component Analysis

A partir de las variables originales, se construyen **combinaciones lineales**. Se buscan las direcciones que maximizan la variabilidad.

Se basa en la idea de que los datos, si bien se encunetran en cierto espacio n-dimensional. estan mayormente dentro de un **subespacio** de menor dimension.

Si tenemos p variables, la primera componente principal (PC1) sera una combinacion lineal de la forma:

$$
Z_1 = \phi_{11} X_1 + \phi_{21} X_2 + ... + \phi_{p1} X_p
$$

donde los coeficientes estan normalizados, es decir:

$$
\sum_{j=1}^{p} \phi_{j1}^2 = 1
$$

y se elige de manera de maximizar la varianza. Dada una muestra i-esima en particular, su proyeccion sobre la componente **PC1** sera:

$$
z_{i1} = \phi_{11} X_{i1} + \phi_{21} X_{i2} + ... + \phi_{p1} X_{ip}
$$

los coeficientes de **PC1** definen la direccion sobre la cual los datos varian mas.

$$
maximize {\frac{1}{n} \sum_{i=1}^{n} (\sum_{j=1}^{p} \phi{j1}x_{ij})^2}
$$

subject to $$\sum_{j=1}^{p} \phi_{j1}^2 = 1$$

La segunda componente, **PC2** es la direccion de **mayor varianza**, dentro de las direcciones **ortogonales** a **PC1**

Asi, hasta la p-esima componente (eran p-variables)
Las direcciones de las componentes principales generar un subespacio que se acerca a los datos.

Por ejemplo, <**PC1, PC2**> representa el plano que esta mas cerca de los puntos (en terminos de distancia euclidea)

## Varianza explicada

Cuanta informacion se preserva? cuanta se pierde? Como lo calculamos?

Podemos considerar la proporcion de varianza explicada (PVE), es decir cuanta varianza explican las componentes, sobre la varianza total.

**Varianza total:**

$$\sum_{j=1}^{p} Var(X_j) = \sum_{j=1}^{p} \frac{1}{n} \sum_{i=1}^{n}x_{ij}^2$$

**Varianza explicada por PCm:**

$$\frac{1}{n} \sum_{j=1}^{n} z_{im}^2 = \frac{1}{n} \sum_{i=1}^{n} (\sum_{j=1}^{p}\phi_{jm}x_{ij})^2$$

**PVE de PCm:**

$$\frac{\sum_{j=1}^{n} z_{im}^2}{\sum_{j=1}^{p} \sum_{i=1}^{n}x_{ij}^2}$$

Tambien se vincula con la distancia al subespacio generado por las componentes principales
