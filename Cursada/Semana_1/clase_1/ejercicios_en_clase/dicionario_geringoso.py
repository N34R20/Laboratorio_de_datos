
diccionario_geringoso = {
    "a": "pa",
    "e": "pe",
    "i": "pi",
    "o": "po",
    "u": "pu",
}

lista = ['banana', 'manzana', 'mandarina']
def geringoso(cadena:str):
    cadena_nueva = ""
    for c in cadena:
        if c in diccionario_geringoso.keys():
            cadena_nueva += c 
            cadena_nueva += diccionario_geringoso[c]
        else:
            cadena_nueva += c
    return cadena_nueva


def traductor_geringoso(lista:list):
    diccionario = dict()
    for elemento in lista:
        diccionario[elemento] = geringoso(elemento)
    return diccionario

print(traductor_geringoso(lista))


