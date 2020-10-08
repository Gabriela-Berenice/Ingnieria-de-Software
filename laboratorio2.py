import random
import numpy as np
import time

puntos = np.random.normal(500,10000000,30)

inicio = time.time()
menor = []

#comparacion de los numeros menores a 500,000

for cantidad in puntos:
    if cantidad < 500000:
        menor.append(cantidad)
        total_puntos = np.sum(menor)

print('Monto total de la suma de los numeros menores a 500,000 es $', total_puntos)
print('Tiempo: {} segundos'.format(time.time() - inicio))
