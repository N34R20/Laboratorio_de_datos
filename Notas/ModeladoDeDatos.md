# Modelado de Datos

Que son los datos?

los datos son el registrio de cosas que existen o han sucedido y tienen un significado implicito

Quienes guardan los datos?
-> Instituciones

De que manera los guardan?
Ejemplo: Bases de Datos

Que es una base de datos?

- Una base de datos es una coleccion de datos relacionados y organizados

- Es una coleccion logicamente coherente de datos con un significado que depende del dominio de aplicacion

## Base de Datos (generales)

- La base de datos es (o deberia ser) independiente de como la almaceno.
- Se diseña, construye y puebla con datos para un proposito especifico:
  - Grupo de usuarios destinatarios.
  - Aplicaciones preconcebidas en las que los usuarios estan interesados.

## Base de Datos (digitales)

- Representan en el mundo virtual algun aspecto del mundo real, un mini-mundo, o el universo de discurso (la parte del mundo en el cual nos enfocamos para representar)

- Los datos que almacenamos son representaciones de cosas del mundo real que queremos almacenar y manipular: son simbolos codificados en diversos formatos

- Una base de datos digital puede ser una coleccion de archivos en algun disco o dispositivo.

## Sistemas de Administracion de Bases de Datos

Una DBMS (Data Base Manager System) es un sistema (de software) desarrollado para el manejo y administracion de bases de datos:

- Capacidad de administrar datos persistentes

- Habilidad de acceder a grandes catidades de datos de manera eficiente

### El DBMS provee, entre otras cosas:

- Soporte para al menos un modelo de datos, permitiendo vistas abstractas a los usuarios
- Soporte para para lenguaje de alto nivel para definir, estructurar y manipular datos, y el acceso a datos (consultas).
- Administracion de transacciones, la habilidad de acceso correcti y concurrente a muchos usuarios a la vez
- Control de acceso, la habilidad de limitar el acceso y chequear la validez de los datos.
- Resiliencia, la habilidad de recuperarse ante fallas del sistema, sin perder datos.

### Principales caracteristicas de una DBMS son:

- Naturaleza autodescriptiva de un sistema de base de datos (catalogo, metadata)

- Aislamiento entre programas y datos, y abstraccion de datos (modelo conceptual)

- Soporte de multiples vistas de los datos

## Modelo de Datos

Un modelo de datos es un modelo (representacion) abstracto que organiza elementos de datos y estandariza como se relacionan tanto entre si como con las propiedades de las entidades del mundo real.

permite ver la informacion no como bits en bruto, sino en terminos mas entendibles para los usuarios.

- Un modelo de datos determina explicitamente la estructura (idealmente solo logica) de los datos

- A menudo se utilizan notaciones en forma grafica

- Suelen ser especificados por un especialista en datos

## Modelo Entidad Relacion

El Diagrama Entidad Relacion (DER) es una herramienta grafica que perimite visualizar entidades del modelo y sus relaciones:

- Ayuda a explicar (visualmente) la estructura logica de una BD.

### PASOS:

1. #### Identificar Entidades

- Una entidad es una cosa del mundo real con una existencia independiente

- Es cualquier cosa del negocio que necesite representarse en la base de datos:

  - Puede ser una cosa fisica, o un hecho sobre el negocio, o un evento qye sucede en el mundo

  - Puede ser una persona, un lugar, un objeto, un evento, o un concepto

- Un conjunto de entidades similares (con las mismas caracteristicas) forma una clase o tipo de entidad:
  - Ej. Persona es una clase de entidad que identfica a todas las cosas que son personas.

2. #### Identificar Atributos

- Cada clase o tipo de entidad posee caracteristicas unicas (atributos) que la representan como tal.

  - Ej. El tipo de entidad Estudiante tiene conceptualmente caracteristicas que la distinguen de un Profesor: el estudiante tiene asociado un numero de libreta, mientras que el profesor tiene asociado un numero de legajo.

- Todas las entidades de una clase o tipo de entidad tienen las mismas caracteristicas pero tienen distintos valores para ellas.

Tipos de atributos

- Atributos simples

- Atributos compuestos

- Atributos derivados

- Atributos multivaluados

3. #### Identificar Claves

4. #### Identificar Relaciones

5. #### Identificar las Cardinalidades

6. #### Identificar Relaciones no binarias

7. #### Identificar Entidades Debiles
