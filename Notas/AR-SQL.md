# Algebra Relacionas - SQL (Structured Query Lenguage)

SQL

- Lenguaje universalmente usado para bases de datos relacionales
- Lenguaje declarativo de alto nivel
- Desarrollado por IBM

Las sentencias SQL se dividen en:

- **Sentencias DDL** (Data Definition Language). Permiten crear/modificar/borrar estructuras de datos -> Tablas. Es tambien donde se definan las restricciones (claves, foreign keys, etc.)

- **Sentencias DML** (Data Manipulation Language). Posibilitan manipular datos. Basado en Algebra relacional

Terminos (Modelo Relacional -> Algebra Relacional )

- Tabla -> Relacion
- Fila -> Tupla
- Columna -> Atributo

## AR <-> SQL

### AR - Proyeccion <-> SQL - SELECT

---

#### **Algebra Relacional**

$$
\pi_{DNI,Salario} (EMPLEADO)
$$

#### SQL

```sql
SELECT DISTINCT DNI, Salario
FROM empleado;
```

---

#### Algebra Relacional

$$
\pi_{Sexo} (EMPLEADO)
$$

#### SQL

```sql
SELECT DISTINCT Sexo
FROM empleado;
```

---

### AR - Seleccion <-> SQL - WHERE

Consigna: Listar de EMPLEADO sólo aquellos cuyo sexo es femenino

#### Algebra Relacional

$$
\sigma_{Sexo=F} (EMPLEADO)
$$

#### SQL

```sql
SELECT DISTINCT *
FROM empleado
WHERE Sexo='F';

```

---

Consigna: Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000

#### Algebra Relacional

$$
\sigma_{Sexo=F \wedge Salario>15.000} (EMPLEADO)
$$

#### SQL

```sql
SELECT DISTINCT *
FROM empleado
WHERE Sexo='F' AND Salario>15000;

```

---

### AR - Renombre <-> SQL - AS

Consigna:

#### Algebra Relacional

$$
EMPLEADO(id,Ingreso) \leftarrow \pi_{DNI,Salario}(EMPLEADO)
$$

#### SQL

```sql
SELECT DISTINCT DNI AS id, Salario AS Ingreso
FROM empleado;
```

---

### AR - Union <-> SQL - UNION

Consigna:

#### Algebra Relacional

$$
ALUMNOS.BD \cup ALUMNOS.TLENG
$$

#### SQL

```sql
SELECT DISTINCT *
FROM alumnos_BD
UNION
SELECT DISTINCT *
FROM alumnos_TLeng;
```

---

### AR - Interseccion <-> SQL - INTERSECT

Consigna:

#### Algebra Relacional

$$
ALUMNOS.BD \cap ALUMNOS.TLENG
$$

#### SQL

```sql
SELECT DISTINCT *
FROM alumnos_BD
INTERSECT
SELECT DISTINCT *
FROM alumnos_TLeng;
```

---

### AR - Minus <-> SQL - EXCEPT

Consigna:

#### Algebra Relacional

$$
ALUMNOS.BD - ALUMNOS.TLENG
$$

#### SQL

```sql
SELECT DISTINCT *
FROM alumnos_BD
EXCEPT
SELECT DISTINCT *
FROM alumnos_TLeng;
```

---

### AR - Interseccion <-> SQL - INTERSECT

Consigna:

#### Algebra Relacional

$$
ALUMNOS.BD \cup ALUMNOS.TLENG
$$

#### SQL

```sql
SELECT DISTINCT *
FROM alumnos_BD
UNION
SELECT DISTINCT *
FROM alumnos_TLeng;
```

---

### AR - Producto Cartesiano <-> SQL - CROSS JOIN

Consigna:

#### Algebra Relacional

$$
PERSONA \times NACIONALIDADES
$$

#### SQL

```sql
SELECT DISTINCT *
FROM PERSONA
CROSS JOIN NACIONALIDADES;
```

---

### AR - Inner Join <-> SQL - INNER JOIN

Consigna:

#### Algebra Relacional

$$
PERSONA \bowtie_{Nacionalidad=IDN} NACIONALIDADES
$$

#### SQL

```sql
SELECT DISTINCT *
FROM PERSONA
INNER JOIN NACIONALIDADES
ON Nacionalidad=IDN;
```

---

### AR - Left Outer Join <-> SQL - LEFT OUTER JOIN

Consigna:

#### Algebra Relacional

$$
PERSONA =\bowtie_{Nacionalidad=IDN} NACIONALIDADES
$$

#### SQL

```sql
SELECT DISTINCT *
FROM PERSONA
LEFT OUTER JOIN NACIONALIDADES
ON Nacionalidad=IDN;
```

---

## SQL - Tuplas espureas

Para que no suceda, la condicion de JOIN SIEMPRE debe ser superclave de una de las tablas que participa del JOIN

## SQL - Funciones de agregacion

- COUNT
- GROUP BY
- ORDER BY
- HAVING -> permite poner condiciones a los valores resultantes de las funciones de grupo

COUNT(). Cantidad de elementos en el grupo.

- MAX(). Máximo registrado en el grupo.
- MIN(). Máximo registrado en el grupo.
- SUM(). Sumatoria correspondiente al grupo.
- AVG(). Promedio correspondiente al grupo

## SQL - LIKE

SQL permite usar comodines a traves de LIKE

## SQL - CASE

## SQL - SUBQUERIES

Operador:

- **IN** -> Retorna TRUE si esta incluido en los valores retornados por la subquery

- **ANY** -> Retorna TRUE si la comparacion es TRUE para al menos un valor retornado por la subquery

- **ALL** -> Retorna TRUE si la comparacion es TRUE para todos los valores retornados por la subquery

- **EXISTS** -> Retorna TRUE si la subquery devuelve al menos una file. FALSE si devuelve 0 filas

## SQL - Manejo de NULLs

- La presencia de nULL genera algunas complicaciones:

  - (NULL > 0) es NULL
  - (NULL + 0) es NULL
  - (NULL = 0) es NULL
  - (NULL AND TRUE) es NULL

- Hay que ser cuidadoso con la clausula WHERE

- En SQL el WHERE elimina cada fila que NO es evaluada como TRUE (es decir, condiciones que son evaluadas como FLASE o NULL se descartan)

- Surge la necesidad de una logica tri-valuada (TRUE, FALSE y NULL)

- Operador espacial para controlar si un valor es nulo (IS NULL o IS NOT NULL)
