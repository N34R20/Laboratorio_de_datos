def tachar_pares(lista:list):

    for i in range(len(lista)):
        if lista[i]%2 == 0:
            lista[i] = 'x'
        else:
            pass
    return lista

print(tachar_pares([1,2,4,5]))