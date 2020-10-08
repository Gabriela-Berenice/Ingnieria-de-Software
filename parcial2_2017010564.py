import random
import numpy as np
import time

puntos = np.random.normal(500,10000000,30)

inicio = time.time()

#comparacion menores  a 500,000

lista_puntos = puntos[puntos < 500000]
total_puntos = np.sum(lista_puntos)

print('Monto total de la suma de los numeros menores a 500,000 es $', total_puntos)
print('Tiempo: {} segundos'.format(time.time() - inicio))
