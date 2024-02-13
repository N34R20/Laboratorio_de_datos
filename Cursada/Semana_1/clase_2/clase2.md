# Clase 2

## Copias

Las listas (y otros objetos) tienen un método para hacer copias. Cuando creamos una copia
b de a, modiﬁcar una no tiene efecto sobre la otra.

```python
a = [2,3,[100,101],4]
b = a.copy()
b == a # True
b is a # False
```

## Diccionarios

Los diccionarios son útiles si vamos a querer buscar rápidamente (por claves).

➔ Se construyen con llaves

➔ Cada entrada tiene una clave y un valor, separados por dos puntitos :

➔ Las entradas se separan con comas

{clave1: valor1, clave2: valor2, … }

➔ Se acceden con corchetes indicando una clave

➔ Tanto las claves como los valores pueden ser de distintos tipos de objetos

➔ Las claves deben ser de tipo inmutable

```python
dias_engl = {'lunes': 'monday', 'martes': 'tuesday', 'miércoles': 'wednesday', 'jueves':
'thursday'}
>>> dias_engl['lunes']
'monday'
>>> dias_engl['viernes']
Traceback (most recent call last):
File "<ipython-input-33-ee0fa133453b>", line 1, in <module>
dias_engl['viernes']
KeyError: 'viernes'
>>> dias_engl['viernes'] = 'friday' # agrego la entrada
>>> dias_engl['viernes']
'friday'

```

## Modulos

Si bien Python tiene muchas funciones que se pueden usar directamente, hay muchas otras que
están disponibles dentro de módulos.

Un módulo es una colección de funciones que alguien (o una comunidad) desarrollaron y
empaquetaron para que estén disponibles para todo el mundo.

Para que las funciones estén disponibles para ser utilizadas en mi programa, tengo que usar la
instrucción import

## Manejo de Archivos

Frecuentemente vamos a utilizar una fuente de datos, que en muchos casos va a estar en un
archivo. Tenemos que poder manejar archivos: leer, crear, modiﬁcar, guardar archivos de distintos
tipos

## Numpy

➔ Colección de módulos de código abierto que tiene aplicaciones en casi todos los campos de las ciencias y de la ingeniería.

➔ Estándar para trabajar con datos numéricos en Python.

➔ Muchas otras bibliotecas de Python (Pandas, SciPy, Matplotlib, scikit-learn, scikit-image, etc) usan numpy.

➔ Objetos: matrices multidimensionales por medio del tipo ndarray (un objeto n-dimensional homogéneo, es
decir, con todas sus entradas del mismo tipo)

➔ Métodos para operar eﬁcientemente sobre las mismas.

Se lo suele importar así:

import numpy as np

## Pandas

- Pandas es una extensión de NumPy para manipulación y análisis de datos.

- Ofrece estructuras de datos y operaciones para manipular tablas de datos
  (numéricos y de otros tipos) y series temporales.

- Tipos de datos fundamentales: DataFrames que almacenan tablas de
  datos y las Series que contienen secuencias de datos.
