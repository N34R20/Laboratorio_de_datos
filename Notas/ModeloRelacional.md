# Modelo Relacional

Diseño de una BD - Etapa del Diseño

Modelo Conceptual

Modelos relacionales

- Tienen base teorica en la teoria de conjuntos y predicados de la logica de primer orden

- Los datos se organizan en una estructura simple: relaciones (tablas)

- Datos se acceden a traves de un lenguaje de alto nievl (operar a nivel conjuntos)

- Almacenamiento fisico queda para la implementacion

## Arquitectura de 3 esquemas

### Nivel Interno

### Nivel Conceptual

### Nivel Externo

### Independencia entre niveles

## Modelo Relacional

representa la base de datos como una coleccion de relaciones (tablas)

Informalmente: - Posee tablas de valores desde cada fila representa una coleccion de valores relacionados - Nombre de la tabla y de las columnas se utiliza para ayudar a interpretar el significado de cada uno de los valores de las filas

Mas formalmente: - Los valores que pueden aparecer en cada atributo (columna) estan representados por un dominio de posibles valores

### Dominio

Conjunto de valores atomicos (cada valor de un dominio es indivisible en lo que al modelo relacional se refiere)

Para cada definición lógica se especiﬁca también un tipo de dato o formato

\*Un dominio cuenta con un nombre, un tipo de dato o formato. Tambien se puede facilitar informacion adicional para la interpretacion de sus valores.

### Esquema

El esquema (o diseño) de la relacion describe la estructura de la relacion (tabla)

Un esquema R denotado por $R(A_1,A_2,....,A_n)$, esta constituido por un nombre de relacion R y una lista de atributos $A_1,A_2,..A_n$

Cada Atributo $A_i$ pertenece a un dominio D y se especifica como $dom(A_i)$

El grado (o arity) de una relacion es la cantidad de atrbutos (n) de la misma

### Estado

Un estado de relacion del esquema $R(A_1,A_2,....,A_n)$, tambien especificado como r(R), es un conjunto de n-tuplas r = {$t_1,t_2,..,t_m$}. Cada tupla t es una lista ordenada de n valores $t = <v_1,v_2, ... ,v_n>$ donde $v_i$, 1 <= i <= n, es un elemento de $dom(A_i)$ o un valor especial NULL

### Caracteristicas

Orden de las tuplas en una relacion

La relacion esta definida como un conjunto de tuplas. Matematicamente los elementos de un conjunto no guardan un orden entre ellos; por lo tanto, las tuplas en una relacion tampoco la tienen.

Orden de los valores dentro de una tupla

El orden de valores dentro de una tupla (y por consiguiente los atributos de un esquema de relación) es importante.

Puede darse una deﬁnición alternativa de una relación que haría innecesaria el ordenamiento de los valores de una tupla, sin embargo usaremos la deﬁnición original de relación, en la que los atributos y los valores de dentro de las tuplas están ordenados, porque simpliﬁca mucho la notación.

Cada valor en una tupla es un valor atómico

El valor no es divisible en componentes -> no están permitidos los atributos compuestos ni multivalor.

Gran parte de la teoría que se esconde tras el modelo relacional fue desarrollada con este principio en mente, el cual recibe el nombre de principio de Primera Forma Normal.

Valores NULLs en las tuplas

tienen varios significados:

- Valor desconocido
- Valor existente pero no disponible
- Atributo no aplicable a esta tupla

### Notacion

- Un esquema de relacion r de grado n se designa como $R(A_1,A_2,....,A_n)$
- Las letras Q, R, S especifican nombres de relacion
- Las letras q, r, s especifican esatdos de relacion
- Las letras t, u , v indican tuplas

En general, el nombre de una relación como ESTUDIANTE va a indicar el conjunto real de tuplas de la misma (el estado actual de la relación) mientras que ESTUDIANTE(Nombre, Apellido, . . .) se va a referir sólo a su esquema

Atributos

Dos atributos (en relaciones diferentes) podrían llegar a tener el mismo nombre. ¿Cómo podemos hacer para diferenciarlos?

Valores

Una n-tupla t en una relación r(R) está designada por t = <v1, v2, . . . , vn>, donde vi es el valor correspondiente al atributo Ai. La siguiente notación se reﬁere a los valores componente de las tuplas:

### Restricciones

**de Dominio**

Las restricciones de dominio especiﬁcan que dentro de cada tupla, el valor de un atributo A debe ser un valor atómico del dominio dom(A).

**de Clave**

Una relación está deﬁnida como un conƧunto de tuplas.
NO. Por deﬁnición, todos los elementos de un conjunto son distintos; por tanto, todas las tuplas en una relación también deben serlo.
Habitualmente existen subconjuntos de atributos (de una relación R) con la propiedad de que dos tuplas (en cualquier relación r de R) no van a tener la misma combinación de valores para estos atributos

i denominamos SK a uno de estos subconjuntos de atributos, entonces para dos tuplas cualesquiera distintas t1 y t2 en una relación r de R, tenemos la restricción: t1[SK] != t2[SK]

**de entidad**

El valor de ninguna clave primaria puede ser NULL

**de integridad referencial**

Informalmente, una tupla de una relación que hace referencia a otra relación debe hacer referencia a una tupla existente de esa relación

**de transicion**

**de dependencia funcional**

Establece una relación funcional entre dos conjuntos de atributos X e ½. Esta restricción especiﬁca que el valor de X determina el de Y en todos los estados de una relación; está indicada como una dependencia funcional X → Y.

### Mapeo desde DER

Como pasar un DER al Modelo Relacional?

#### PASOS:

#### 1. Tipo de Entidades Fuertes

- a) Por cada tipo de entidad (fuerte) E del DER, crear una relacion R que incluya todos los atributos simples de E (para el caso de atributos compuestos, incluir unicamente los atributos simples que los componen)

- b) seleccionar los atributos que componen la clave de E como clave principal de R.

#### 2. Tipo de Entiedades Debiles

- a) Por cada tipo de entidad (débil) E del DER y cuyo tipo de entidad propietaria es P, crear una relación R que incluya todos los atributos simples de E (para el caso de los atributos compuestos, incluir únicamente los atributos simples que los componen)

- b) Incluir en R los atributos correspondientes a la clave P (estos atributos van a conformar una foreing key)

- c) Seleccionar tanto los atributos que componen la clave de E, como los atributos que componen la clave de P, y designarla como clave primaria de R

#### 3. Relacion uno-a-uno (1:1)

Hay 3 opciones:

1. **Metodologia de la foreign key**

   Seleccionar una de las relaciones ya mapeadas (por ejemplo S) e incluya como foreign key en S la clave primaria de T. Lo mejor es elegir, en el papel de S, un tipo de entidad con participacion total en R. Incluir todos los atributos simples (o las componentes simples de los atributos compuestos) del tipo de relacion 1:1 de R como atributos de S.

2. **Metodologia de la relacion mezclada**

   Fusionar los dos tipos de entidad (S y T) y la relacion en una sola relacion. Esto puede ser apropiado cuando las dos participaciones son totales.

3. **Metodologia de referencia cruzada o relacion de relacion**

   Crear una tercera relacion R con el proposito de crear una referencia cruzada de las claves primarias de las relaciones S y T que represnetan los tipos de entidad.

#### 4. Relacion muchos-a-muchos (N:M)

Crear una nueva relacion S para representar a la relacion R. Incluir como atributos de la foreing key en S las claves primarias de las relaciones que representan los tipos de entidad particulares; su combinacion formara la clave primaria de S. Incluya tambien cualquier atributos simple del tipo de relacion N:M y los atributos de S

#### 5. Relacion uno-a-muchos (1:N)

Identificar la relacion S que representa el tipo de entidad participante en el lado N del tipo de relacion. Incluir como foreign key en S la clave primaria de la relacion T que representa el otro tipo de entidad participante en R; esto es porque cada instancia de entidad en el lado N esta relacionada, a lo sumo, con una instancia de entidad del lado 1 del tipo de relacion. Incluya cualesquiera atributos simples (o componentes simples de los atributos compuestos) del tipo de relacion 1:N como atributos de S.

#### 6. Relacion n-aria

Crear una nueva relacion S para representar R.
Incluir como atributos de la foreign key en S las claves primarias de las relaciones que representan los tipos de entidad participantes.
Incluir tmabien atributos simples del tipo de relacion n-aria como astributos de S. Normalmente la clave primaria de S es el conjunto de todas las foreign keys que referencias a los tipos de entidad participantes. No obstante, si la cardinalidad en cualquiera de los tipos de entidad E que participan en R es 1, entonces la clave primaria de S no debe incluir el atributo de la foreing key que hace referencia a E
