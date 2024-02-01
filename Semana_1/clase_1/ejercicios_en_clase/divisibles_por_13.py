"""
Escribir un programa que imprima en pantalla los números enteros entre 0 y
213 que sean divisibles por 13
"""

def divisibles_13(numero:int):
    divisibles = list()
    for i in range(numero):
        if i % 13 == 0:
            divisibles.append(i)

        else:
            pass

    return divisibles

print(divisibles_13(213)) 