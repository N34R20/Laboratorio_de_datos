nombre_archivo = 'cronograma_sugerido.csv'

with open(nombre_archivo, 'rt') as file:
    for line in file:
        datos_linea = line.split(',')
        print(datos_linea[1])