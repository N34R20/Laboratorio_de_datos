"""
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra.
Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'.
Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes programadores'.
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