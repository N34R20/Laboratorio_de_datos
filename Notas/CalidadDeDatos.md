# Calidad de Datos

- Un dato o conjunto de datos X tiene mayor calidad que un dato o conjunto de datos Y, si X satisface las necesidades del usuario mejor que Y.

## Consecuencia de contar con datos de mala calidad:

- Desconfianza
- Insatifaccion de los clientes
- Costos innecesarios
- Impacto en la toma de decisiones

## Problemas habituales

- Valores no estandarizados
- Valores imposibles o poco probables
- Valores faltantes
- Valores desactualizados
- Ocurrencias duplicadas
- Falta de datos historicos
- Incosistencia entre aplicaciones o en una misma aplicacion
- Infromacion critica que no es confiable.

## Causas de problemas

1. Problemas asociados a la **INSTANCIA**

   - Datos que han cambiado en el mundo real, y que no fueron actualizados
   - Datos que provienen de distintas fuentes, deberian ser consistentes y sin embargo no lo son
   - Datos que no han sido almacenados con la precision necesaria

2. Problemas asociados al **MODELO DE DATOS**

   - Si se detecta que hay informacion que no esta presente porque no hay forma de almacenarla

   -> el modelo de datos fisico esta incompleto

   - El mundo que se quiere representar evoluciono y no se tradujeron los cambios al modelo.

   -> perdida de vigencia del modelo

3. Problemas asociados a los **PROCESOS**

   - Distintas personas cargan la misma informacion haciendo distintas asunciones

   - Se carga con una asuncion y se usa otras

   - Modificaciones manuales pro procesos

   - Gente que hace modificaciones pero no deberia estar autorizada para hacerlas

4. Problemas asociados a los **ERRORES DE SOFTWARE**

   - Datos obligatorios que no se asumen como tales y por lo tanto no se cargan

   - Interfaces poco amigables

## Atributos de Calidad

1. Completitud

   - Estan presentes todos los valores para representar la realidad

   - Estan presentes todas las instancias existentes en el mundo real

2. Relevancia

   - Los datos son relevantes para representar la realidad

3. Vigencia

   - Los datos se mantienen actualizados con la frecuencia adecuada

4. Disponibilidad

   - Los datos estan accesibles

5. Confiabilidad

   - Se puede considerar que los datos representan informacion veridica

   - No hay contradicciones entre distintos datos almacenados

6. Correccion

   - Los datos representan la situacion real

7. Seguridad/Privacidad

   - Los datos son solo accesibles por los usuarios autorizados

   - Los datos cumplen con los requerimientos de privacidad adecuados de acuerdo a la reglamentacion nacional-internacional/criterios eticos.

# Calidad

## Cuan buenos son los datos

Como determinar cuan buena es la calidad de los datos?

tenemos que entender cuales son lso <u>datos criticos</u> y para ellos determinar los atributos de calidad de interes

Seguir una metodologia

1. Hacer relevamiento
2. Elaborar metricas de calidad
3. Recolectar valores de dichas metricas

-> nos va a permitir **cuantificar** la calidad

### 1. Hacer relevamiento

Objetivo: Determinar: - Datos criticos - Ciclo de vida del dato - Atributos de interes

Tareas: - Identificar stakeholders - Conseguir compromiso por parte del clinete - Leer documentacion sobre los sistemas, sobre el negocio, y estudiar modelos de datos - Hacer cuestionarios tendientes a determinar cuales son los datos criticos, cual es el ciclo de vida del dato, cuales son los atributos de interes y los problemas habituales - Llevar adelante los cuestionarios con cada uno de los stakeholders

### 2. Elaborar metricas de calidad

### GQM (Goal Question Metric)

### 3. Recolectar valores
