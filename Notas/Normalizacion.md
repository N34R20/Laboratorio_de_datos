# Normalizacion

INDICE:

1. [Introduccion](#introduccion)
2. [Pautas de diseño](#pautas-de-diseño)
3. [Dependencias Funcionales](#dependencias-funcionales)
4. [Definicion General de 2FN y 3Fn / BFCN](#definicion-general-de-2fn-y-3fn--bcfn)

## Introduccion

## Pautas de Diseño

### Pauta Nro. 1 - Semantica

- Semantica: sucnato mas facil es explicar la semantica de los esqumas, mejor es el diseño

- Diseñar esquemas tal que sea facil de explicar su signiﬁcado

- No combinar atributos de diversos tipos de entidades y relaciones en una misma relacion

### Pauta Nro. 2 - Almacenamiento

- Objetivo: Minimazar espacio de almacenamiento a traves del diseño

- Anomalias de actualizacion. almacenar NATUARL JOINs introduce problemas adicionales.

1. Anomalias de Insercion

2. Anomalias de Delecion

3. Anomalias de Modificacion

4. Anomalias de Insercion

- Pauta Nro. 2

  - Diseñar un esquema tal que no permitan anomalias de insercion, delecion y modificacion
  - Si permiten anomalias, señalarlas claramente y asegurar que programas que actualizan BD operaran correctamente

- Performance
  - Notar que esta pauta puede ser violada en favor de la performance
  - En tal caso se debe señalar y actuar en consecuencia (Ej: triggers/store procedures que realicen automaticamente actualizaciones)

### Pauta Nro. 3 - NULLs

### Pauta Nro. 4 - Tuplas Espureas

## Dependencias Funcionales

Proposito: Herramienta formal para el analisis de esquemas. Permite detectar y describir problemas descritos previamente

Informalmente: Restriccion entre dos conjutnos de atributos X e Y de una BD. Los valores que toman los atributos de Y dependen de los valores que tomen X

Formalmente:

- Esquema relacional de la BD posee n atributos $A_1, A_2, ..., A_n$
- Pensar toda la BD descripta por un solo esquema universal R = { $A_1, A_2, ..., A_n$}. Esto no implica que realmente la BD se almacene como una tabla universal. Solo se usara este concepto para construir la teoria formal de las dependencias de datos.

- Definicion:
  - Sean X e Y dos conjuntos de atributos incluidos en R
  - La dependencia funcional (DF) indicada como X -> Y especifica una restriccion sobre las posibles tuplas que pueden conformar una instancia r de R
  - Restriccion: para cualquiera dos tuplas t1 y t2 en r tal que t1[X] = t2[X] , se debe cumplir t1[Y] = t2[Y]

propiedades:

Si X es clave candidata (CK) de R, entonces X → Y ∀
subconjunto de atributos Y de R.
Si X es CK de R, entonces X → R.

- Semantica

- Diseño

- Instancias legales

- Inferencia de DF

## Formas Normales (FN) basadas en Clave Primaria (PK)

- Se asume

  -
  -

- Proceso de Normalizacion

  -
  -

- Normalizacion de los datos

  -
  - -
    -
  -

- Definicion

### Introduccion

### 1FN

Tecnicas para alcanzar 1FN

### 2FN

### 3FN

## Definicion General de 2FN y 3Fn / BCFN

### 2FN

Definicion general : Un esquema R esta en 2FN si todo atributo no primo de A de R no depende paricalmente (de manera funcional) de niguna clave de R

Definicion alternativa : Un esquema R esta en 2FN si todo atributo no primo de A de R depende completamente (de manera funcional) de todas las claves de R

### 3FN

Definicion general : Un esquema R esta en 3FN si, para toda dependencia funcional _no trivial_ X -> A de R, se cumple alguna de las siguientes condiciones:

- X es SK de R
- A es atributo primo de R

DF trivial: La DF A -> B es trivial si B es un subconjunto de atrbutos de A.
Ej: A -> A es una DF trivial

Admite Redundancia

### BCFN

Definicion: Un esquema R esta en BCFN si, para toda dependencia funcional _no trivial_ X -> A de R, X es SK de R

BCFN vs 3FN: BCFN es mas restrictiva que 3FN ya que BCFN no permite que A sea primo

## introduccion

### Inferencia

Reglas de inferencia:

"Axiomas de Armstrong"

- Rl1 (regla reflexiva): Si $Y \subseteq X$ Entonces $X \rightarrow Y$
- Rl2 (regla de incremento) {$X \rightarrow Y$} $\models XZ \rightarrow YZ$
- Rl3 (regla transitiva) {$X \rightarrow Y, Y \rightarrow Z$} $\models X \rightarrow Z$
- Rl4 (regla de descomposicion o proyeccion)
- Rl5 (regla de union o aditiva)
- Rl6 (regla de pseudotransitiva)

### Clausura y equivalencia

### Conjunto minimal de DFs

## Propiedades de la Descomposicion

Descomposicion: Es la descomoposicion de R en un conjunto de esquemas D={$R_1, R_2, ..., R_m$} de R

Propiedad deseable Nro 1: Se desea preservacion de atributos

$$
\bigcup_{i=1}^{m} R_i = R
$$

### Preservacion de atributos

### Preservacion de DFs

Propiedad deseable Nro 2: Si X -> Y en F, es deseable que o bien aparezca en algun esquema $R_i$ de D o bien pueda ser inferida de ls DFs de algun esquema $R_i$

Importante:

Proyeccion:

Preservacion de DFs:

### Lossless Join

- **Lossless Join informalmente**: El cumplimiento de esta propiedad no permite la generacion de tuplas espureas cuando se realiza un NATURAL JOIN entre las relaciones resultantes de una descomposicion

- **Lossless Join formalmente**: Una descomposicion D={$R_1, R_2, ..., R_m$} de R posee la propiedad **_lossless join_** con respecto al conjutno de DFs de R si, para todo estado r(R) que satisface F, se cumple que $\bowtie(\pi_{R_1}(r), ...., \pi_{R_m}(r))=r$

## Algoritmos para el Diseño de Esquemas

### Algoritmo D1 - 3FN

- **Algoritmo Nro. D1**: Descomposicion en 3FN

Entrada: R universal y un conjunto de DFs F sobre R

1. Hallar el cubrimiento minimal G de F (utilizar algoritmo ya dado)

2. Para cada lado izquierdo X de cada DF que aparece en G
   Crear una relacion D con atributos $\{ X\cup \{A_1 \} \cup \{A_2 \} \cup ... \cup \{A_k \}\}$, siendo $X\rightarrow A_1, X\rightarrow A_2, ..., X\rightarrow A_k,$ las unicas dependencias en G con X como lado izquierdo (X es la clave en esta relacion)

3. Si ninguna relacion D contiene una clave R
   Entonces crear una relacion adicional en D que contenga atributos que formen una clave de R (se puede utilizar algoritmo ya dado)

4. Eliminar relaciones redundantes de D. Una relacion R de D es redundante si R es una proyeccion de otra relacion S de D.

Descompone relacion universal R cumpliendo:

- 3FN
- Preservacion de DFs
- Lossles Join

### Algoritmo D2 - BCFN
