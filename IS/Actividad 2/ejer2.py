import numpy as np
import time 

#Se importa los archivos de texto
books = np.genfromtxt('libros_24_meses.txt')
lista = np.genfromtxt('catalogo_libros.txt')

inicio = time.time()

#Filtro
filtro = list(filter(lambda n: n in books, lista))
print(len(filtro))
print('Tiempo: {} segundos'.format(time.time() - inicio))
