import random
import numpy as np
import time

puntos = np.random.normal(500,30,10000000)

inicio = time.time()
menor = []

#comparacion de los numeros menores a 500,000
for valor in puntos:
    if valor < 500000:
        menor.append(valor)
        total_puntos = np.sum(menor)

print('Monto total de la suma de los numeros menores a 500,000 es $', total_puntos)
print('Tiempo: {} segundos'.format(time.time() - inicio))
