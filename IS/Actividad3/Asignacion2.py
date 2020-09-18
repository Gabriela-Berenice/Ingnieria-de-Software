#importar librerias
import numpy as np
import time

#abrir documento txt
lista = np.genfromtxt('costos.txt')

inicio = time.time()

#comparacion menores o iguales a 25
lista_costos = lista[lista <= 25]
monto_total = np.sum(lista_costos)
print('Monto total de seleccion es $', monto_total)
print('Tiempo: {} segundos'.format(time.time() - inicio))