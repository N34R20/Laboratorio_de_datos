altura_inicial = 100

"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.
"""

salto = 3/5
def rebotes(salto:float, altura_inicial:float):
    for i in range(10):
        print(round(altura_inicial * salto, 4))
        altura_inicial = altura_inicial * salto

rebotes(salto=3/5, altura_inicial=altura_inicial)