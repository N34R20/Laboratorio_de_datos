#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:47:12 2024

@author: admin
"""

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

import string
#%%
"""
Ejercicio 1
Analisis Exploratorio de Datos

"""
df = pd.read_csv("sign_mnist_train.csv")

caracteres = list(string.ascii_lowercase)
print(len(caracteres))

def map_labels_with_characters(characters:list, df:pd.DataFrame):
    
    d = dict()
    for i in range(len(characters)):
        d[i] = characters[i]
        
    df['character'] = df['label'].map(d)
    
    # shift column 'Name' to first position 
    first_column = df.pop('character') 
      
    # insert column using insert(position,column_name, 
    # first_column) function 
    df.insert(0, 'character', first_column) 
    
    return df

df = map_labels_with_characters(characters=caracteres, df=df)
#%%

print(df.head(10))
print("\n")
print(df.shape)

"""
Hay un total de 27455 imagenes y cada imagen esta compuesta por 784 pixeles -> 28^2 = 784
"""
#%%

images, labels = df.iloc[:, 2:], df['character']

# Displaying 16 random images
def displayImg(images, title):
    plt.figure(figsize = (15, 10))
    
    for i in range(len(images)):
        plt.subplot(4, 4, i + 1)
        plt.title(title[i])
        plt.imshow(np.reshape(images[i], (28, 28)), cmap = 'gray')
        plt.axis('off')
    plt.show()
    
rand = np.random.randint(0, images.shape[0] - 16)
displayImg(images.iloc[rand:rand + 16].values, labels.iloc[rand:rand + 16].values)


#%%

print(df.character.value_counts())

#%%
"""
a. ¿Cuáles parecen ser atributos relevantes para predecir la letra a la que 
corresponde la seña? ¿Cuáles no? ¿Creen que se pueden descartar atributos?
"""

promedios = np.zeros((24,784))
X = [i for i in range(784)]
#fig, ax = plt.subplots()
fila = 0

for num in range(26):
    df_letra = df[df['label'] == num]
    if df_letra.size > 0:
        descripcion_letra = df_letra.describe()
#print(descripcion_letra_a.iloc[2,1:])
        promedios_letra = descripcion_letra.iloc[2,1:]
        promedios[fila,:] = promedios_letra
        fila += 1
    #ax.plot(X, promedios_letra)

#print(X)

#%%
desvios = []
for i in range(784):
    desvios.append(np.std(promedios[:,i]))
print(desvios)

#%%

fig, ax = plt.subplots()
ax.plot(X,desvios)


#%%
"""
b. ¿Hay señas que son parecidas entre sí? 
Por ejemplo, ¿Qué es más fácil de diferenciar: 
la seña de la E, de la seña de la L o la seña de la E de la seña de la M?
"""

X = [i for i in range(784)]

letra_E = df[df['character']=='e']
descripcion_letra_e = letra_E.describe()
promedios_letra_e = descripcion_letra_e.iloc[2,1:] #tomamos la fila de promedios

letra_L = df[df['character']=='l']
descripcion_letra_l = letra_L.describe()
promedios_letra_l = descripcion_letra_l.iloc[2,1:] #tomamos la fila de promedios

letra_M = df[df['character']=='m']
descripcion_letra_m = letra_M.describe()
promedios_letra_m = descripcion_letra_m.iloc[2,1:] #tomamos la fila de promedios

#fig,ax = plt.subplots()
#ax.plot(X,promedios_letra_e)
#ax.plot(X,promedios_letra_l)

# la E y la L parecen tener señas similares, voy a comparar con la M

fig,ax = plt.subplots()
ax.plot(X,promedios_letra_e)
ax.plot(X,promedios_letra_m)

#print(promedios_letra_e)
#print(promedios_letra_l)


#%%
"""
c. Tomen una de las clases, por ejemplo la seña correspondiente a la C, 
¿Son todas las imágenes muy similares entre sí?
"""


c_sign = df[df['character'] == 'c']

print(c_sign.iloc[1,2:])

for i in range(5):
    plt.imshow(np.reshape(c_sign.iloc[i,2:], (28, 28)), cmap = 'gray')
    plt.show()
    
"""
Respuesta: En su mayoria si, cambia la forma de la mano en muchos casos, y la altura de la mano, 
cosa que pueda confundir un algoritmo al buscar pixeles especificos 
"""

#LO DE ARRIBA ES DE FRAN, HAGO OTRA COSA ABAJO PORQUE HAY QUE JUSTIFICAR LO DICHO CON GRÁFICOS

#%%

letra_C = df[df['character']=='c']
"""
descripcion_letra_c = letra_C.describe()
print(descripcion_letra_c)
desvios_c = descripcion_letra_c.iloc[2,1:]
"""
X = [i for i in range(784)]

fig,ax = plt.subplots()
filas = letra_C.iloc[:,0].size

for i in range(10):
    ax.plot(X,letra_C.iloc[i,:])
#%%
"""
d. Este dataset está compuesto por imágenes, 
esto plantea una diferencia frente a los datos que utilizamos en las clases 
(por ejemplo, el dataset de Titanic). ¿Creen que esto complica la exploración de los datos?
"""

"""
Respuesta: Si, la complica, sobretodo porque los datos al ser no estructurados 
no tienen atributos especificos, con lo cual las caracteristicas 
son simplemente el gradiente de los pixeles individuales.
"""

#%%
"""
Ejercicio 2
Dada una imagen se desea responder la siguiente pregunta: 
¿la imagen corresponde a una seña de la L o a una seña de la A?
"""
#%%
"""
a. A partir del dataframe original, construir un nuevo dataframe que
contenga sólo al subconjunto de imágenes correspondientes a señas
de las letras L o A.
"""
df_ej_2 = df[(df['character'] == 'a') | (df['character'] == 'l')]

#%%
"""
b. Sobre este subconjunto de datos, analizar cuántas muestras se tienen
y determinar si está balanceado con respecto a las dos clases a
predecir (la seña es de la letra L o de la letra A).
"""
# Printeamos las muestas de cada caracter y su proporcion sobre el total
l_count = df_ej_2.character.value_counts()['l']
a_count = df_ej_2.character.value_counts()['a']
proporcion_l = l_count / (l_count + a_count)
proporcion_a = a_count / (l_count + a_count)
print("Cantidad de muestras 'L': ", l_count, " corresponde a ", "%.3f"%proporcion_l, " del dataset")
print("Cantidad de muestras 'A': ", a_count, " corresponde a ", "%.3f"%proporcion_a, " del dataset")

# Consideramos que esta balanceado ya que casi hay un 50% de muestras de cada clase
#%%
"""
c. Separar os datos en conjuntos de train y test.
"""

X = df_ej_2.iloc[:,2:]
y = df_ej_2.iloc[:, 0:1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

#%%
"""
d. Ajustar un modelo de KNN considerando pocos atributos, por ejemplo 3. 
Probar con distintos conjuntos de 3 atributos y comparar resultados.
Analizar utilizando otras cantidades de atributos.
"""
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

print(clf)
#%%
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, recall_score, precision_score

grid = GridSearchCV(LinearSVC(dual="auto"), param_grid={'C': [1, 10]},scoring=ftwo_scorer, cv=5)
clf.fit(X_train, y_train)



#%%
"""
Ejercicio 3
(Clasificación multiclase) 
Dada una imagen se desea responder la siguiente pregunta: 
¿A cuál de las vocales corresponde la seña en la imagen?

"""
#%%
"""
a. Vamos a trabajar con los datos correspondientes a las 5 vocales. 
Primero filtrar solo los datos correspondientes a esas letras. 
Luego, separar el conjunto de datos en train y test.
"""

df_ej_3 = df[  (df['character'] == 'a') 
             | (df['character'] == 'e')
             | (df['character'] == 'i') 
             | (df['character'] == 'o') 
             | (df['character'] == 'u')]

print(df_ej_3.character.value_counts())

#sSplit del dataset
from sklearn.model_selection import train_test_split
X = df_ej_3.iloc[:,2:]
y = df_ej_3.iloc[:, 0:1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y['character'])

#%%
"""
b. Ajustar un modelo de árbol de decisión. Analizar distintas profundidades.
"""
from sklearn.tree import DecisionTreeClassifier

# Utilizamos Manual Search para analizar tres profundidades distintas 

arbol1 = DecisionTreeClassifier(max_depth = 6)
arbol2 = DecisionTreeClassifier(max_depth = 11)
arbol3 = DecisionTreeClassifier(max_depth = 16)

# Entrenamos los modelos

arbol1.fit(X_train, y_train)
arbol2.fit(X_train, y_train)
arbol3.fit(X_train, y_train)

# Calculamos el score para cada modelo

score_train_1 = arbol1.score(X_train, y_train)
score_test_1 = arbol1.score(X_test, y_test)

score_train_2 = arbol2.score(X_train, y_train)
score_test_2 = arbol2.score(X_test, y_test)

score_train_3 = arbol3.score(X_train, y_train)
score_test_3 = arbol3.score(X_test, y_test)

# Printeamos el score de cada modelos para poder compararlos

print("Arbol con max_depth = 6:", "\n  Score con dataset de Train: ", score_train_1,
      "\n  Score con dataset de Test: ", score_test_1)
print("Arbol con max_depth = 11:", "\n  Score con dataset de Train: ", score_train_2,
      "\n  Score con dataset de Test: ", score_test_2)
print("Arbol con max_depth = 16:", "\n  Score con dataset de Train: ", score_train_3,
      "\n  Score con dataset de Test: ", score_test_3)

#%%
"""
c. Para comparar y seleccionar los árboles de decisión,
utilizar validación cruzada con k-folding.
Importante: Para hacer k-folding utilizar los datos del conjunto de train.
"""
from sklearn.model_selection import GridSearchCV

# Creamos un arbol de decisión
arbol_cv = DecisionTreeClassifier(random_state = 8)


# Definimos que hiperparametros vamos a probar utilizando Grid Search
hyper_params = {'criterion' : ["gini", "entropy"],
                'max_depth' : [i for i in range(6,17,1)]}

# Creamos los modelos que vamos a entrenar con sus respectivos hiperparametros y
# utilizando 5 StratifiedKFolds
clf = GridSearchCV(arbol_cv, hyper_params, cv = 5, verbose = 2, return_train_score = True)

# Entrenamos los modelos
clf.fit(X_train, y_train)

#%%
"""
d. ¿Cuál fue el mejor modelo? 
Evaluar cada uno de los modelos utilizando el conjunto de test. 
Reportar su mejor modelo en el informe. 
OBS: Al realizar la evaluación utilizar métricas de clasificación multiclase. 
Además pueden realizar una matriz de confusión y evaluar los distintos tipos de errores para las clases.
"""
import itertools
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Asignamos y printeamos los mejores parametros encontrados con el Cross Validation
mejores_parametros = clf.best_params_
print("Mejores parametros encontrados: ", mejores_parametros)

# Finalmente evaluamos el modelo con los mejores parametros
# Calculamos el score
print("Score del arbol con mejores parametros:", "\n  Score con dataset de Train:", clf.best_score_,
      "\n  Score con dataset de Test: ", clf.best_estimator_.score(X_test, y_test))

# Creamos una matriz confusion para visualizar el error por clase
y_true = [i for i in y_test['character']]
y_pred = clf.best_estimator_.predict(X_test)
matriz_confusion = confusion_matrix(y_true, y_pred, labels=['a','e','i','o','u'])

# Hacemos un plot para visualizarla
disp = ConfusionMatrixDisplay(confusion_matrix=matriz_confusion,
                              display_labels=clf.classes_)

disp.plot()
plt.show()

# Asignamos el score a cada parametro del Cross Validation
params = clf.cv_results_['params']
score = clf.cv_results_['mean_test_score']
for i in range(len(params)):
    params[i]['score'] = score[i]
resultados_cv = params
# print("Lista de diccionarios con el score de cada modelo:", *resultados_cv, sep="\n  ")
# Lo dejamos comentado para que no ensucie el output, pueden descomentarlo para
# ver los resultados del Cross Validation

# Creamos el modelo final con los mejores parametros encontrados
arbol_final_modelo = DecisionTreeClassifier(criterion = mejores_parametros['criterion'],
                                     max_depth = mejores_parametros['max_depth'])

# Entrenamos el modelo final con TODO el dataset. Estimamos que su performance es igual
# o ligeramente mejor por haberlo entrenado con un dataset ligeramente mas grande
arbol_final = arbol_final_modelo.fit(X, y)

