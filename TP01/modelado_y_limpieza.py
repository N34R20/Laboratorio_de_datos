#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:26:35 2024

@author: admin
"""



#%%
import pandas as pd
from inline_sql import sql_val, sql


carpeta = "TablasOriginales/"


#%%
tablas_originales = dict()

gdp = pd.read_csv(carpeta+"API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv")
gdp_metadata = pd.read_csv(carpeta+"Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv")
lista_sedes_datos = pd.read_csv(carpeta+"lista-sedes-datos.csv")
lista_secciones = pd.read_csv(carpeta+"lista-secciones.csv")
lista_sedes = pd.read_csv(carpeta+"lista-sedes.csv")

tablas_originales['gdp'] = gdp
tablas_originales['gdp_metadata'] = gdp_metadata
tablas_originales['lista_sedes_datos'] = lista_sedes_datos
tablas_originales['lista_secciones'] = lista_secciones
tablas_originales['lista_sedes'] = lista_sedes_datos

"""
Printeamos todas las columnas
"""
print(tablas_originales.keys())

def print_columns(tablas:dict)-> None:
    for df in tablas.keys():
        print(f"columnas de {df}:\n {tablas[df].columns.tolist()}\n")
        
print_columns(tablas=tablas_originales)

#%%

seccion = lista_secciones[['sede_id', 'sede_desc_castellano']]
seccion.columns = ['Id_sede', 'Descripcion']

filtro_distinc =  """
                  SELECT DISTINCT *
                  FROM seccion
                  """
                  
seccion = sql^filtro_distinc
seccion.to_csv('TablasLimpias/seccion.csv', index=False)



#%%
pbi = gdp[['Country Name', 'Country Code', '2022']]
gdp_metadata = gdp_metadata[['Country Code', 'Region']]

pais = pbi.merge(gdp_metadata, on='Country Code', how='left')
pais.columns = ['Pais', 'Id_pais', 'PBI', 'Region']

pais = pais.dropna(subset=['Region'])

pais.to_csv('TablasLimpias/pais.csv', index=False)



#%%
sede = lista_sedes[lista_sedes['estado'] != 'Inactivo']

sede = sede[['sede_id', 'sede_desc_castellano', 'pais_iso_3']]
sede.columns = ['Id', 'Descripcion', 'Id_pais']

sede.to_csv('TablasLimpias/sede.csv', index=False)


#%%

print("Cantidad de nulls en la columna de redes sociales: ", lista_sedes_datos['redes_sociales'].isna().sum())

lista_sedes_datos['redes_sociales'] = lista_sedes_datos['redes_sociales'].astype(str).apply(lambda x: x.split(' '))  
lista_sedes_datos['redes_sociales'] = lista_sedes_datos['redes_sociales'].apply(lambda x: [value for value in x if value != "//" and value != ""])
lista_sedes_datos['redes_sociales'] = lista_sedes_datos['redes_sociales'].apply(lambda x: 'nan' if 'nan' in x else x)



lista_sedes_datos = lista_sedes_datos[lista_sedes_datos['redes_sociales'] != 'nan']

red_social = lista_sedes_datos.explode('redes_sociales')

red_social = red_social[['sede_id', 'redes_sociales']]
red_social.columns = ['Id_sede', 'Url']

red_social['Nombre_red'] = red_social['Url'].apply(lambda x: x.split('//')[-1].split('/')[0])
red_social['Nombre_red'] = red_social['Nombre_red'].apply(lambda x: 'www.instagram.com' if x.startswith('@') else x)
red_social['Nombre_red'] = red_social['Nombre_red'].apply(lambda x: 'www.instagram.com' if x == 'instagram.com' else x)
red_social['Nombre_red'] = red_social['Nombre_red'].apply(lambda x: 'www.facebook.com' if x == 'facebook.com' else x)
red_social['Nombre_red'] = red_social['Nombre_red'].apply(lambda x: 'www.twitter.com' if x == 'twitter.com' else x)

def parse_red_social(url:str):
    if url.startswith('www.'):
        url = url.split('.')[1].capitalize()
    return url

red_social['Nombre_red'] = red_social['Nombre_red'].apply(parse_red_social)

red_social_filtro = """
                    SELECT *
                    FROM red_social
                    WHERE Url LIKE '%@%' OR Url LIKE '%.com%'
                    """
red_social = sql^red_social_filtro

red_social.to_csv('TablasLimpias/red_social.csv', index=False)



#%%

seccion = pd.read_csv('TablasLimpias/seccion.csv')
pais = pd.read_csv('TablasLimpias/pais.csv')
sede = pd.read_csv('TablasLimpias/sede.csv')
red_social = pd.read_csv('TablasLimpias/red_social.csv')

#%%

"""
Reportes SQL
"""

#%%
"""
Ejercicio 1
"""

query1 = """
        SELECT  p.Pais, COUNT(s.id) as sedes, p.PBI, Subq.secciones_promedio
        FROM sede s
        JOIN pais p ON s.Id_pais = p.Id_pais
        LEFT JOIN (
            SELECT p.Id_pais, AVG(cant_secciones) as secciones_promedio, 
            FROM (SELECT sec.id_sede, COUNT(sec.id_sede) as cant_secciones, s.Id_pais
                  FROM seccion sec
                  LEFT JOIN sede s ON s.Id = sec.Id_sede
                  GROUP BY sec.id_sede, s.Id_pais) AS subquery
            JOIN pais p ON subquery.Id_pais = p.Id_pais
            GROUP BY p.Id_pais) AS Subq
        ON p.Id_pais = Subq.Id_pais
        GROUP BY s.Id_pais, p.PBI, p.Pais, Subq.secciones_promedio;
        """
ejercicio1 = sql^query1


#%%
"""
Ejercicio 2
"""

query2 = """
        SELECT p.Region AS region, AVG(p.PBI) as promedio_PBI
        FROM sede s
        LEFT JOIN pais p ON s.Id_pais = p.Id_pais
        WHERE p.Region IS NOT NULL
        GROUP BY p.Region;

        """
ejercicio2 = sql^query2

#%%
"""
Ejercicio 3
"""

query3 = """
            SELECT p.Pais, COUNT(DISTINCT Nombre_red) as cant_de_redes_diferentes     
            FROM red_social r
            JOIN sede s ON r.Id_sede = s.Id
            JOIN pais p ON s.Id_pais = p.Id_pais
            GROUP BY p.Pais
            ORDER BY cant_de_redes_diferentes DESC;
            
            """
     

ejercicio3 = sql^query3

#%%

"""
Ejercicio 4
"""

query4 = """
        SELECT p.Pais, s.Id as Sede, r.Nombre_red as Red_Social, r.Url as URL
        FROM red_social r
        JOIN sede s ON r.Id_sede = s.Id
        JOIN pais p ON s.Id_pais = p.Id_pais;
        
        """
ejercicio4 = sql^query4


#%%

"""
Visualizaciones
"""
import matplotlib.pyplot as plt
import seaborn as sns

#%%
"""
Ejercicio 1

"""
query5 = """
        SELECT p.Region AS region, COUNT(region) as cant_sedes
        FROM sede s
        LEFT JOIN pais p ON s.Id_pais = p.Id_pais
        WHERE p.Region IS NOT NULL
        GROUP BY p.Region
        ORDER BY cant_sedes DESC;

        """
        
sede_por_region = sql^query5
print(type(sede_por_region))

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.bar(sede_por_region['region'], sede_por_region['cant_sedes'],  alpha=0.9, color='orange')

# Set labels and title
plt.xlabel('Region')
plt.ylabel('Numero de Sedes')
plt.title('Numero de Sedes por Region')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
#%%

"""
Ejercicio 2

"""
query6 = """
        SELECT  p.PBI, p.Region
        FROM sede s
        JOIN pais p ON s.Id_pais = p.Id_pais
        WHERE p.PBI IS NOT NULL
        GROUP BY s.Id_pais, p.PBI, p.Pais, p.Region
        ORDER BY PBI DESC;

        """
        
pbi_region = sql^query6

median_pbi_by_region = pbi_region.groupby('Region')['PBI'].median().sort_values()

cmap = sns.color_palette("viridis", as_cmap=True)

plt.figure(figsize=(10, 6))
sns.boxplot(data=pbi_region, x='Region', y='PBI', order=median_pbi_by_region.index, palette = "husl")

# Set labels and title
plt.xlabel('Region')
plt.ylabel('PBI')
plt.title('Boxplots del PBI por Region')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')


#%%
"""
Ejercicio 3

"""
query7 = """
        SELECT  p.Pais, p.PBI, COUNT(p.Pais) as cant_sedes, 
        FROM sede s
        JOIN pais p ON s.Id_pais = p.Id_pais
        WHERE p.PBI IS NOT NULL
        GROUP BY s.Id_pais, p.PBI, p.Pais, p.Region
        ORDER BY cant_sedes DESC;

        """
        
pbi_pais = sql^query7

plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
sns.scatterplot(data=pbi_pais, x='cant_sedes', y='PBI', alpha=0.9, hue='Pais', legend=False, size='cant_sedes', sizes=(20, 2000))

# Set labels and title
plt.xlabel('Numero de Sedes')
plt.ylabel('PBI')
plt.title('Relacion entre el numero de Sedes y el PBI')

#%%

print(lista_secciones.sede_id.value_count())
