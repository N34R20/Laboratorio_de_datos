"""
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po',
o 'pu' según corresponda luego de cada vocal.
"""

diccionario_geringoso = {
    "a": "pa",
    "e": "pe",
    "i": "pi",
    "o": "po",
    "u": "pu",
}

cadena = "Geringoso"
capadepenapa = ""
for c in cadena:
    if c in diccionario_geringoso.keys():
        capadepenapa += c 
        capadepenapa += diccionario_geringoso[c]
    else:
        capadepenapa += c

print(capadepenapa)

