
Ejercicios:

a) Descargar los datos

b) Determinar forma normal en la que se encunetran

c) Plantear Objetivo general del trabajo

d) Generar un DER para los datos necesarios

e) Generar en python dataframes vacios correspondiente al DER (en 3FN), para cada uno definir:

    - Clave primaria (PK)

    - Dependencias Funcionales (DF)
    
    - Claves foraneas (FK)

f) Importar los datos a los esquemas, elavorando procesos de mejora de los datos. Describir los problemas de calidad detectados

Para cada uno de los datatsets y cada problema de calidad debe mencionar:

    - el atributo de la calidad afectado
    
    - si el problema corresponde a modelo y/o a instancia

    - una medida concreta acerca de la magnitud del problema (metodo GQM)

Finalmente, describir en cada caso que criterios utilizaron para corregir los datos y como impacta en la calidad

g) Importar los datos (limpios) a los esquemas. 

h) Generar reportes usando SQL:

4 reportes en total

    i) Para cada país informar cantidad de sedes, cantidad de secciones en promedio que poseen sus sedes y el PBI per cápita del país en 2022. El orden del reporte debe respetar la cantidad de sedes (de manera descendente). En caso de empate, ordenar alfabéticamente por nombre de país.

    ii) Reportar agrupando por región geográfica: 
    
    a) la cantidad de países en que Argentina tiene al menos una sede y 
    
    b) el promedio del PBI per cápita 2022 de dichos países. Ordenar por el promedio del PBI per Cápita


    iii) Para saber cuál es la vía de comunicación de las sedes en cada país, nos hacemos la siguiente pregunta: ¿Cuán variado es, en cada el país, el tipo de redes sociales que utilizan las sedes? Se espera como respuesta que para cada país se informe la cantidad de tipos de redes distintas utilizadas. Por ejemplo, si en Chile utilizan 4 redes de facebook, 5 de instagram y 4 de twitter, el valor para Chile debería ser 3 (facebook, instagram y twitter).
    
    iv) Confeccionar un reporte con la información de redes sociales, donde se indique para cada caso: el país, la sede, el tipo de red social y url utilizada. Ordenar de manera ascendente por nombre de país, sede, tipo de red y finalmente por url


i) Mostrar, utilizando herramientas de visualizacion, la siguiente info:

    i) Cantidad de sedes por región geográfica. Mostrarlos ordenados de manera decreciente por dicha cantidad.

    ii) Boxplot, por cada región geográfica, del PBI per cápita 2022 de los países donde Argentina tiene una delegación. Mostrar todos los boxplots en una misma figura, ordenados por la mediana de cada región.

    iii) Relación entre el PBI per cápita de cada país (año 2022 y para todos los países que se tiene información) y la cantidad de sedes en el exterior que tiene Argentina en esos países.