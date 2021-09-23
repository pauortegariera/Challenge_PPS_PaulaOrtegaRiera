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

## PARTE 1.2 - ESTADÍSTICAS SOBRE CLASES DE UN DATAFRAME DE IMÁGENES.


## CARGA DE DATOS #####


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

## FUNCIÓN PARA OBTENER DATOS ESTADÍSTICOS SOBRE LAS IMÁGENES ANALIZADAS##

def var_clases(clases):
    """
    Función para identificar la imagen con mayor diversidad de clases.Además se obtiene
    la imagen con mayor cantidad de eventos y la cantidad de clases de esa imagen.
    Permite obtener la clase que más se repite en todas las imágenes analizadas.
    Por último, obtiene un histograma que compara la distribución de las clases que más
    se repiten en las imágenes analizadas.
    (Obtiene los números únicos en una lista.)
    Parameters:
    clases: Lista con las clases de la imagen.
    Returns:
    Lista con la cantidad y el tipo de clases distintas en la imagen.
    Path de la imagen analizada.
    Máxima cantidad de eventos en una imagen, clases en imagen con máxima cantidad de 
    eventos,clases que más se repiten, histograma que compara la repeticiones de las clases.
    
    """
    
    var_clases = [] # Almacena la cantidad de clases encontradas en cada dataFrame
   
    for i in clases:
         unique_n = np.unique(i) # Valores únicos de clases de cada dataFrame.
         var_clases.append(unique_n)        
    var_img = var_clases # Clases encontradas en cada dataFrame.

    cant=[] # Se obtiene la mayor cantidad de clases distintas.

    for i in var_img:
        cant_var=np.size(i)
        cant.append(cant_var)

    for i in cant:
        máx_var=np.max(cant) # Mayor variedad de clases encontrada en una imagen.
    
    Ruta_abs=os.path.abspath(__file__)
    
    var_eventos=[] # Almacena la cantidad de eventos que se producen en una imagen.
    
    for i in clases:
        cant_eventos= np.size(i) # Obtiene el tamaño de la cantidad de eventos de cada dataFrame. 
        var_eventos.append(cant_eventos) 
    
    eventos=var_eventos # Cantidad de eventos en una imagen.
    
    for i in eventos:
        máx_event=np.max(eventos) # Obtiene la máxima cantidad de eventos registrados en una imagen.

    for i in eventos:
        clases_max_ev= np.where(eventos==máx_event)[0] # Índice de la lista que contiene el array con máxima cantidad de eventos.
    
    
    for i in clases_max_ev:
        unique_ev = np.unique(i)
   
    repet=[] # Almacena la clase que se repite más veces en cada imagen. 

    for i in clases:
        repeticiones = mode(i) # Obtiene la moda de cada dataFrame.
        repet.append(repeticiones)
    
    máx_rep=mode(repet) # Obtiene la clase que más se repite en todas las imágenes.
    
    
    clases_all=[] #Almacena todas las clases detectadas en todos los dataFrames cargados.

    clases_all=np.block(var_clases) # Concatena todas las listas de clases de cada dataFrame.
            
## PARTE 2 - HISTOGRAMA ##

    plt.hist(clases_all, bins=len(var_img),color = 'grey',ec="black") # Obtiene el histograma para cada dataFrame.
    plt.xlabel('Clases')                                             # Por el momento es necesario introducir el 
    plt.ylabel('Cantidad de apariciones')                            # índice del dataFrame a graficar.
    plt.title('Distribución de aparición de clases en datos ingresados')
    plt.show() 
            
   
    return (máx_var,Ruta_abs,máx_event,máx_rep,var_clases,clases_all)

mvar,ruta,mevent,m_rep,var_clases,tipos=var_clases(clases)

print('La mayor variedad de clases en una imagen es de',mvar,'clases.') 
print('Esa imagen se encuentra en la ruta:',ruta)
print('La mayor cantidad de eventos en una imagen es', mevent,'eventos.')
#print('Esa imagen tiene',cant_clases,'clases')
print('La clase que más se repite en el total de las imágenes analizadas es la correspondiente al número', m_rep,'.')
print('En la sección "PLOTS" se encuentra un histograma de las clases que aparecen en el dataset.')


# PARTE 3 - FUNCIÓN PARA INTERCAMBIAR CLASES.

 
def swap(clases):
    
    """
    Función para intercambiar clases en una imagen.
    Parameters:
    clases2 : Lista que contiene los txt cargados.
    clase1: Valor de clase que se quiere cambiar.
    clase2: Valor de clase por el que se quiere cambiar.
    Returns: Lista con el reemplazo de valores realizado.

    
    """

    direc= input('Ingrese el path del dataset a analizar:') #Se pide al usuario
    
    fileDir = direc  # Dirección del directorio
    fileExt = r'.txt' # Extensión de los archivos deseados del directorio
   
    files=[_ for _ in os.listdir(fileDir) if _.endswith(fileExt)] # Buásqueda de los archivos a analizar
    
                                              
    data2=[] # Almacena los datos de cada dataFrame cargado.

    for file in files:
        df2 = pd.read_csv(file, delimiter= ' ', 
        index_col=None, header= None).sort_index(axis=0, 
        level=None, ascending=True, inplace=False) # Lee los dataFrame.
        data2.append(df2)

    clases2=[] # Almacena las primeras columnas de cada dataFrame, es decir, sus clases.

    for i in range(len(data2)):
        clases2.append(data2[i][0]) 
         
        
    clase1= int(input('ingrese el número correspondiente a la clase que desea cambiar:'))
    clase2= int(input('ingrese el número correspondiente de la clase por la cual va realizar el cambio:' ))
    reemplazo=[item.replace(clase1, clase2) for item in clases2] # Se realiza el reemplazo.
    
    return(data2,df2,clases2,clase1,clase2,reemplazo)

data2,df2,clases2,clase1,clase2,reemplazo=swap(clases)
                                                                        
print('Reemplazo realizado.')


