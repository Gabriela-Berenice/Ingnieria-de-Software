import numpy as np
import time 

books = np.genfromtxt('libros_24_meses.txt')
lista = np.genfromtxt('catalogo_libros.txt')

filtro = list(filter(lambda n: n in books, lista))
print(len(filtro))
