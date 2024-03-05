# Algebra Relacional

1. [Introduccion](#introduccion)

2. [Operaciones Unarias](#operaciones-unarias)

3. [Operaciones Binarias](#operaciones-binarias)

# Introduccion

**Def**: Lenguaje formal utilizado en el modelo relacional

- Permite a usuarios especificar consultas sobre instancias de relaciones.

- El resultado de una consulta es una nueva relacion.

- **Importante**
  1. Provee fundamento formal a las operaciones aosciadas al modelo relacional
  2. Base para implenetar y optimizar querys en RDBMS
  3. Principales operaciones y funcionaes de los modulos internos de la mayoria de los sitemas relacionales estan en operaciones de AR

-**Tecnica** procedural (a diferencia del **Calculo Relacional** que es de tipo declarativo)

# Operaciones Unarias

## AR - SELECT

- **Fucnion**. Selecciona un subconjunto de tuplas de una relacion que satisface cierta condicion
- **Notacion**. $\sigma$ <condicion de seleccion > (R)

### Propiedades

- **Operador Unario**. Se aplica a una sola relacion

- **Grado**. $ Grado(\sigma_c(R)) = Grado(R)$

- **# tuplas**. $ Grado(\sigma_c(R)) = Grado(R)$

- la fraccion de tuplas seleccionadas se denomina selectividad de la condicion

- **Conmutatividad**

- Cascada de SELECTs

- SQL

## AR - PROJECT

- **Funcion**

- **Notacion** $ $

### Propiedades

- **Operador Unario**. Se aplica a una sola relacion

- **Grado**. $ $

- **# tuplas**.

- **Conmutatividad**

- Cascada de SELECTs

- SQL

## AR - RENAME (Cont.)

- **Funcion**

- **Notacion** $ $

### Propiedades

- **Operador Unario**.

- **Grado**. $ $

- **# tuplas**. $ $

- **Conmutatividad**

- Cascada de SELECTs

- SQL

# Operaciones Binarias

## AR - UNION, INTERSECTION, MINUS

- **Funcion**

- **Notacion** $ $

### Propiedades

- **Operador Unario**.

- **Grado**. $ $

- **# tuplas**. $ $

- **Conmutatividad**

- Cascada de SELECTs

- SQL

## AR - CARTESIAN PRODUCT / JOIN

- **Funcion** produce una nueva relacion que combina cada tupla de una relacion con cada una de las tuplas de la otra relacion

- **Notacion** $ R X S $

### Propiedades

- **Union compatible** las relaciones no tienen que ser union compatibles

- **Grado**. $ $

- **# tuplas**. $ $

- **Conmutatividad**

- Cascada de SELECTs

- SQL Croos

## AR - JOIN

- **Funcion** Permite combinar pares de tuplas relacionadas entre dos relaciones

- **Notacion** $ $

### Propiedades

- **Operador Unario**.

- **Grado**. $ $

- **# tuplas**. $ $

- **Conmutatividad**

- Cascada de SELECTs

- SQL

## AR - DIVISION

- **Funcion**

- **Notacion** $ $

### Propiedades

- **Operador Unario**.

- **Grado**. $ $

- **# tuplas**. $ $

- **Conmutatividad**

- Cascada de SELECTs

- SQL
