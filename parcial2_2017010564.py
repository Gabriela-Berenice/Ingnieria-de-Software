import random
import numpy as np
import time

puntos = np.random.normal(500,10000000,30)

inicio = time.time()
#comparacion menores o iguales a 500000

lista_puntos = puntos[puntos < 500000]
puntos_tot = np.sum(lista_puntos)

print('Monto total de la suma de los numeros menores a 500,000 es $', puntos_tot)
print('Tiempo: {} segundos'.format(time.time() - inicio))
