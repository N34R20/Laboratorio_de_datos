# Normalizacion

INDICE:

1. [Introduccion](#introduccion)
2. [Pautas de diseño](#pautas-de-diseño)
3. [Dependencias Funcionales](#dependencias-funcionales)
4. [Definicion General de 2FN y 3Fn / BFCN](#definicion-general-de-2fn-y-3fn--bcfn)

## Introduccion

- **Salida del Diseño** Conjunto de relaciones

- **Calidad de Diseño** Necesidad de evaluar si una forma de agrupar atributos en un esquema es mejor que otra

- **Niveles**

  - **Logico (o Conceptual)**. Un buen diseño de esquemas a este nivel habilita a los usuarios a entender el significado de los datos de las relaciones

  - **Implementacion (o de Almacenamiento Fisico)**. Como se almacenan y actualizan las tuplas

- **Objetivos**

  - **Preservar la Informacion**
  - **Minimizar la Redundancia**

## Pautas de Diseño

Cuatro pautas informales de diseño pueden utilizarse como medida para determinar la calidad de un diseño:

1. Estar seguro que semantica de atributos en esquemas es clara
2. Reducir la informacion redudante en tuplas
3. Reducir la cantidad de valores NULL en tuplas
4. Desabilitar la posibilidad de generar tuplas espureas

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

- Definicion: La **forma normal** de una relacion refiere a la mayor forma normal alcanzada por ella

- Se asume

  - Se cuneta con el conjunto de DF para cada relacion
  - Cada relacion tiene designada su Clave Primaria (PK)

- Proceso de Normalizacion

  - A cada esquema ejecutarle una serie de test para **certificar** que satisface una **forma normal**

- Normalizacion de los datos

  - Proceso de analizar los esquemas, basandose en DF y PK
  - Objetivo: lograr propiedades deseables
    - Minimizar redundancia
    - Minimizar anomalias de insercion, delecion, y modificacion
  - Esquemas que no pasan ciertos test de formas normales, se descomponen en esquemas mas pequeños que pasan el test (y sus propiedades)

### Introduccion

Sin garantıa. Las formas normales, consideradas aisladas de otros factores, no garantizan un buen diseño de la BD

Propiedades. Luego de proceso de normalizacion por descomposicion

- Nonadditive Join (Lossless Join). Garantıa de que no ocurre problema de generacion de tuplas espureas

- Preservacion de DF. Garantıa de que cada DF se encuentra representada en algun esquema resultante de la descomposicion
  Lossless Join debe lograrse a cualquier costo

Preservacion de DF. Es deseable, pero en algunos casos es sacriﬁcada

- **Super Clave (SK)**. Una SK de R = {$A_1, A_2, ..., A_n$} es un subconjunto de atributos $S\subseteq R$ con la propiedad de que no hay dos tuplas $t_1, t_2$ en un estado legal r(R) que cumplan $t_1(S)=t_2(S)$

- **Clave (K)**. Una clave K es una SK con la propiedad adicional de que al remover cualquier atributo de K, deja de ser SK. Es decir, K es una SK _minimal_.

- **Clave Candidata (CK)**. Si un esquema posee mas de una clave, cada una de ellas se denominan clave candidata.

- **Clave Primaria (PK)**. Una de las CK es designada arbitrariamente como PK

- **Clave Secundaria**. CK que no es PK

- **Atributo primo**. Atributo de un esquema R que pertenece a **alguna** CK de R

- **Requisito**. En la practica, todos los esquemas deben poseer PK

---

### 1FN

- **Prohibe** relaciones dentro de relaciones o relaciones como valores de atributos dentro de tuplas.

- **Admite**. El dominio de un atributo debe incluir solo valores atomicos (simples e indivisibles). En la tupla, puede tomar 1 solo valor del dominio.

#### Tecnicas para alcanzar 1FN

1. Remover atributo que viola 1FN y ubicarlo en una nueva relacion. La nueva relacion tiene como PK ambos atributos -> mejor solucion, no sufre de redundancia y es generica (no se limita a un maximo de valores posibles)

**Recursividad**. La tecnica se puede utilizar recursivamente para multiples niveles

### 2FN

- **DF Completa**. Una DF X → Y es Completa si al eliminar algun atributo A de X la DF deja de existir

- **DF Parcial**. Una DF X → Y es Parcial si es posible eliminar algun atributo A de X y la DF continua existiendo

Tips.

- Para testear 2FN hay que veriﬁcar solo DFs cuyos lado izq. posean atributos que sean parte de la PK

- Si la PK se compone de un solo atributo, entonces no es necesario realizar ningun test

---

### 3FN

- **Dependencia Transitiva**: Una DF $X \rightarrow Y$ en R es Transitiva, si existe un conjunto de atributos Z en R que no son ni Clave Candidata (CK) ni un subconjunto de alguna Clave de R, tal que
  $X \rightarrow Z$ y $Z \rightarrow Y$

Un esquema R esta en 3FN si esta en 2FN y ningun atributo no primo de R depende transitivamente de la PK

---

## Definicion General de 2FN y 3Fn / BCFN

- **2FN / 3FN**. Tienen en cuenta todas las claves candidatas

- **1FN**. Modificacion no afecta a 1FN ya que es independiente de claves

- **Atributo Primo**. Atributo que es parte de alguna CK

### 2FN

**Definicion general** : Un esquema R esta en 2FN si todo atributo no primo de A de R no depende paricalmente (de manera funcional) de niguna clave de R

**Definicion alternativa** : Un esquema R esta en 2FN si todo atributo no primo de A de R depende completamente (de manera funcional) de todas las claves de R

### 3FN

**Definicion general** : Un esquema R esta en 3FN si, para toda dependencia funcional _no trivial_ X -> A de R, se cumple alguna de las siguientes condiciones:

- X es SK de R
- A es atributo primo de R

**DF trivial**: La DF A -> B es trivial si B es un subconjunto de atrbutos de A.
Ej: A -> A es una DF trivial

Admite Redundancia

### BCFN

**Definicion**: Un esquema R esta en BCFN si, para toda dependencia funcional _no trivial_ X -> A de R, X es SK de R

**BCFN vs 3FN**: BCFN es mas restrictiva que 3FN ya que BCFN no permite que A sea primo

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
