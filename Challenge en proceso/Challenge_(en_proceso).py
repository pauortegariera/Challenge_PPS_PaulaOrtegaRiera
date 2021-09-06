#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:03:54 2021

@author: paulaortegariera
"""

from glob import glob
import pandas as pd
import numpy as np
import os
from statistics import mode
import matplotlib.pyplot as plt

files = glob('00*.txt') # Contiene todos los archivos que comiencen con "00" y 
                        #terminen en la extensión ".txt" ubicados en la carpeta
                        #donde se encuentra el script.

files.sort() # Ordena los txt cargados.

data=[] # Almacena los datos de cada dataFrame cargado de los archivos txt.

for file in files:

    df = pd.read_csv(file, delimiter= ' ', 
    index_col=None, header= None).sort_index(axis=0, 
    level=None, ascending=True, inplace=False) # Lee los dataFrame.
    data.append(df)

clases=[] # Almacena las primeras columnas de cada dataFrame, es decir, sus clases.

for i in range(len(data)):
    clases.append(data[i][0])
    

def var_clases(clases):
    """
    Función para identificar la imagen con mayor diversidad de clases.
    (Obtiene los números únicos en una lista.)
    Parameters:
    clases: Lista con las clases de la imagen.
    Returns:
    Lista con la cantidad y el tipo de clases distintas en la imagen.
    """
    
    var_clases = [] # Almacena la cantidad de clases encontradas en cada dataFrame
   
    for i in clases:
         unique_n = np.unique(i) # Valores únicos de clases de cada dataFrame.
         var_clases.append(unique_n)
    return var_clases

var_img = var_clases(clases) # Clases encontradas en cada dataFrame.


cant=[] # Se obtiene la mayor cantidad de clases distintas.

for i in var_img:
        cant_var=np.size(i)
        cant.append(cant_var)

for i in cant:
    máx_var=np.max(cant) # Mayor variedad de clases encontrada en una imagen.
    

Ruta_abs=os.path.abspath(__file__)
path, filename = os.path.split(Ruta_abs)


print('La mayor cantidad de clases en una imagen es de',máx_var,'clases.') 
print('Esa imagen se encuentra en la ruta {}'.format(path)) 

def var_eventos(clases):
    
    """
    Función para identificar la mayor cantidad de eventos en una imagen.
    (Obtiene los el tamaño de una lista y busca la lista de mayor tamaño.)
    Parameters:
    clases: Lista con las clases de la imagen.
    Returns:
    Lista con la cantidad de eventos y la máxima cantidad de eventos registrada.
    """
    
    var_eventos=[] # Almacena la cantidad de eventos que se producen en una imagen.
    
    for i in clases:
        cant_eventos= np.size(i) # Obtiene el tamaño de la cantidad de eventos de cada dataFrame. 
        var_eventos.append(cant_eventos) 
    return var_eventos

eventos=var_eventos(clases) # Cantidad de eventos en una imagen.

for i in eventos:
    máx_event=np.max(eventos) # Obtiene la máxima cantidad de eventos registrados en una imagen.


"""
Éstas líneas tenían por finalidad obtener las clases existentes en la lista donde se cumple
que existe el máximo número de eventos. Sin embargo no funciona, calculo que por algún error 
de sintáxis que no alcancé a corregir.


clases_max_ev=np.where(eventos==máx_event)[0] # Índice de la lista que contiene el array
                                        # con máxima cantidad de eventos.
                                        #(el elemento que contiene el índice en la tupla)                                     
for i in clases:
    unique_ev = np.unique(i)

    
"""    
    
print('La mayor cantidad de eventos en una imagen es',máx_event,'eventos.')
print('Esa imagen se encuentra en la ruta {}'.format(path))

   
repet=[] # Almacena la clase que se repite más veces en cada imagen. 

for i in clases:
    repeticiones = mode(i) # Obtiene la moda de cada dataFrame.
    repet.append(repeticiones)
    
máx_rep=mode(repet) # Obtiene la clase que más se repite en todas las imágenes.



print('La clase que más se repite en el total de las imágenes analizadas es', máx_rep)

       
plt.hist(clases[1], bins=len(var_img),color = 'grey',ec="black") # Obtiene el histograma para cada dataFrame.
plt.xlabel('Clases')                                             # Por el momento es necesario introducir el 
plt.ylabel('Cantidad de apariciones')                            # índice del dataFrame a graficar.
plt.title('Distribución de clases en una imagen')
plt.show()                                                   
  
                                                              
  

