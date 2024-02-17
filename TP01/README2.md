#### Datos
1) Plantear objetivo del trabajo
2) se necesitan datos para cumplir el objetivo del trabajo: 
	1) definir qué datos de las fuentes de datos necesitamos y que vamos a hacer con ellas
3) Armar un DER, utilizando solo lo necesario para resolverlo. alimentas el esquema con los datos limpios que necesitamos
#### Ejercicios (DOCUMENTAR LO MAS POSIBLE TODO EL PROCESO)
1) Descargar los datos y comprenderlos
2) En que forma normal se encuentran? justificar
3) Plantear el objetivo del trabajo
4) Generar DER con los datos necesarios para resolver el problema planteado
5) generar en python dataframes vacios, que esten en 3FN y documentar:
	1) clave primaria
	2) dependencias funcionales (conjunto minimal)
	3) claves foraneas
6) Detectar los problemas de calidad de datos en los datasets importados (al menos uno de cada fuente, tienen que ser problemas distintos). mencionar:
	1) el atributo de la calidad afectado
	2) si el prblema corresponde a modelo y/o a instancia
	3) una medida concreta acerca de la magnitud del problema (utilizav GQM y explicar bien cada paso)
	4) explicar en cada caso qué criterios tomamos para corregir los datos y como estas acciones impactaron en la calidad de ellos (nuevas metricas)
7) importar los datos a los dataframes vacios que creamos. documentar desde qué fuentes de datos se está haciendo
8) generar reportes utilizando solo consultas SQL (SI EL REPORTE RESUME INFORMACION COMENTAR LOS RESULTADOS OBSERVADOS)
	1) para cada pais, informar:
		1) cantidad de sedes (de manera descendente, en caso de empate que esté alfabeticamente por nombre de pais)
		2) cantidad de secciones en promedio que poseen sus sedes
		3) informar PBI per capitas del pais en 2022
	2) agrupar por region geografica
		1) la cantidad de paises donde argentina tiene al menos una sede
		2) promedio del PBI per capita 2022 en dichos paises (ordenar por este atributo)
		3) informar por cada pais la cantidad de TIPOS de redes sociales distintas utilizadas
		4) confeccionar tabla donde se indique para cada caso: de manera ASC por pais, sede, tipo de red social, url
			1) pais
			2) sede
			3) tipo de red social
			4) url
9)  utilizando herramientas de visualizacion, mostrar: (COMENTAR LOS OBSERVADO EN CADA GRAFICO)(AGREGAR EN CADA GRAFICO SEPARADOS DE MILES)
	1) cantidad de sedes por region geografica, ordenados de manera decreciente por dicha cantidad (explicar porque elegimos la forma de representarla)
	2) boxplot por cada region geografica del PBI per capita 2022 de los paises donde argentina tiene una delegacion. que este en una misma figura, ordenados por la mediana de cada region
	3) relacion entre el PBI per capita de cada pais y la cantidad de sedes en el exterior que tiene Argentina en esos paises
10) CONCLUSION responder la pregunta principal de los objetivos del trabajo. en caso de no haberlo hecho, decir qué informacion falta y mostrarla. enumerar y mostrar los resultados

#### Formato del informe
1) maximo 14 paginas A4 en Arial 11 en pdf
2) Codigo (archivo .py)
	1) encabezado
		1) nombre de los integrantes del grupo
		2) descripcion del contenido
		3) datos que puedan ser relevantes
	2) en cada seccion debe haber un comentario que explique el codigo y "debe poder correrse desde cualquier maquina"
	3) las variables usadas deben tener nombre representativo (nada de a1 = ...)
	4) las tablas originales y las resultantes de nuestro trabajo deben ser entregadas con el resto del tp, cada una en formato CSV
	5) las tablas originales deben estar en una carpeta "TablasOriginales" y las limpias en una carpeta "TablasLimpias"
Secciones
	1) Caratula
		1) nombre de la materia
		2) titulo del tp
		3) miembros
	2) Seccion resumen
		1) sintesis de la problematica, trabajo realizado y conclusiones (TLDR)
	3) Seccion introduccion
		1) intro del problema a resolver
		2) objetivo general del trabajo
		3) actividades a realizar para alcanzar el objetivo
		4) resumen de la resolucion y de como continua el informa
	4) seccion procesamiento de Datos
		1) mencionar en qué forma normal se encontraban los datos originales
		2) lo procesos para aumentar su calidad
		3) la documentacion del DER y su representacion en el modelo relacional
		4) descripcion del proceso de importacion (imagino que de los datos a los dataframes vacios que creamos)
	5) Seccion desiciones tomadas
		1) que desiciones tomamos xd
	6) seccion analisis de datos
		1) respuestas a las preguntas planteadas en los ejercicios de las tablas con SQL y visualizacin de datos
		2) si las tablas son muchas o largas, se pueden incorporar en una seccion nueva seccion ANEXO o en un archivo csv
	7) seccion conclusiones
#### Entrega
1) Completar planilla de autoevaluacion (una por grupo) y descargarla como pdf
2) Por el campus en un .ZIP con nombre "TP01-nombredelgrupo.zip" (se encarga Nehuen) 
	1) documento .pdf del informe
	2) archivo .py,
	3) ambas carpetas con las tablas (originales y limpias)
	4) planilla de autoevaluacion
3) informe Impreso + planilla de autoevaluacion

 