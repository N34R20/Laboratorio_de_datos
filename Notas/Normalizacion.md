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

### 3FN

### BCFN

## introduccion

### Inferencia

### Clausura y equivalencia

### Conjunto minimal de DFs

## Propiedades de la Descomposicion

### Preservacion de atributos

### Preservacion de DFs

### Lossless Join

## Algoritmos para el Diseño de Esquemas

### Algoritmo D1 - 3FN

### Algoritmo D2 - BCFN
