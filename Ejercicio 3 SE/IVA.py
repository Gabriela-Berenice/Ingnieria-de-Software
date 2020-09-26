import numpy as np
import time

#abrir documento txt
lista = np.genfromtxt('costos.txt')

inicio = time.time()

#comparacion menores o iguales a 25
lista_costos = lista[lista < 25]
monto_total = np.sum(lista_costos)
IVA = monto_total*0.13
print('Monto de la seleccion sin IVA es: $', monto_total)
print('IVA(13%): $', IVA)
print('El Total es: $', monto_total+IVA)
print('Tiempo: {} segundos'.format(time.time() - inicio))