 
import pandas as pd
import numpy as np
from statistics import mode
import matplotlib.pyplot as plt

df= pd.read_csv('0000002_00005_d_0000014.txt', delimiter=' ',index_col= None, header= None ) # Se realiza la carga del data frame.
df.iloc[:,0:1] # se selecciona la columna de interés, en este caso, la de clases de objetos.
lista_clases=df[0].tolist() # se convierte la columna seleccionada en una lista.

"""
unique, counts = np.unique(lista_clases, return_counts=True)
máx_clase=np.max(unique)

print(dict(zip(unique, counts)))

print('la clase que más aparece es',máx_clase)

"""

#print(mode(lista_clases))

# 4

plt.hist(lista_clases,bins=range(len(lista_clases.unique()+1)),color="grey",ec="black") º