

#---------------
# Ejercio 1
#---------------
print("EJERCICIO 1")

"""
Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir
de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente.
¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el
obelisco? Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m.
"""

def duplicar_billetes():
    pass

#---------------
# Ejercio 2
#---------------
print("EJERCICIO 2")

"""
Una pelota de goma es arrojada desde una altura de 100 metros 
y  cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa rebotes.py que imprima una tabla mostrando 
las alturas que alcanza en cada uno de sus primeros diez rebotes.
"""

altura_inicial = 100
salto = 3/5
def rebotes(salto:float, altura_inicial:float):
    for i in range(10):
        print(round(altura_inicial * salto, 4))
        altura_inicial = altura_inicial * salto


rebotes(salto=3/5, altura_inicial=altura_inicial)

#---------------
# Ejercio 3
#---------------
print("EJERCICIO 3")

"""
Queremos hacer un traductor que cambie las palabras masculinas de una frase
por su versión neutra. Como primera aproximación, completá el siguiente código
para reemplazar todas las letras 'o' que ﬁguren en el último o anteúltimo caracter
de cada palabra por una 'e'
"""

frase = 'todos somos programadores'
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    
    if palabra[-1] == 'o': 
        palabra = list(palabra)
        palabra[-1] = 'e'
        palabra = ''.join(palabra)
        frase_t += palabra + ' '

    elif palabra[-2] == 'o':
        palabra = list(palabra)
        palabra[-2] = 'e'
        palabra = ''.join(palabra)
        frase_t += palabra + ' '

    else:
        frase_t += palabra + ' '


print(frase_t)

#---------------
# Ejercio 4
#---------------
print("EJERCICIO 4")

"""
Deﬁnir una función es_par(n) que devuelva True si el número es par y False en
caso contrario.
"""
def es_par(n:int):
    if n%2 == 0:
        return True
    else:
        return False

print(es_par(2))
print(es_par(3))
#---------------
# Ejercio 5
#---------------
print("EJERCICIO 5")

"""
Deﬁnir una función dos_pertenece(lista) que tome una lista de enteros y
devuelva True si la lista tiene al 2 y False en caso contrario.
"""
def dos_pertenece(lista:list):
    pass
#---------------
# Ejercio 6
#---------------
print("EJERCICIO 6")

"""
Deﬁnir una función pertenece(lista, elem) que tome una lista y un
elemento, y devuelva True si la lista tiene al elemento dado y False en caso
contrario
"""
def pertenece(lista:list, elem):
    pass
#---------------
# Ejercio 7
#---------------
print("EJERCICIO 7")

"""
Deﬁnir una función mas_larga(lista1, lista2) que tome dos listas y
devuelva la más larga.
"""
def mas_larga(lista1:list, lista2:list):
    pass
#---------------
# Ejercio 8
#---------------
print("EJERCICIO 8")
"""
Deﬁnir una función cant_e que tome una lista de caracteres y devuelva la
cantidad de letras 'e' que tiene la misma.
"""
def cant_e():
    pass
#---------------
# Ejercio 9
#---------------
print("EJERCICIO 9")

"""
Deﬁnir una función sumar_unos que tome una lista de enteros, les sume 1 a
todos sus elementos, y devuelva la misma lista, pero modiﬁcada.
"""
def sumar_unos():
    pass
#---------------
# Ejercio 10
#---------------
print("EJERCICIO 10")

"""
Deﬁnir la función mezclar(cadena1, cadena2) que tome dos strings y
devuelva el resultado de intercalar elemento a elemento. Por ejemplo: si
intercalamos Pepe con Jose daría PJeopsee. En el caso de Pepe con Josefa daría
PJeopseefa.
"""
def mezclar():
    pass