import random
import numpy as np
import time

puntos = range(500,10000000,30)

inicio = time.time()
menor = []

lista_menores = map(int, puntos)

#comparacion de los numeros menores a 500,000
for valor in lista_menores:
    if valor < 500000:
        menor.append(valor)
        total_puntos = np.sum(menor)

print('Monto total de la suma de los numeros menores a 500,000 es $', total_puntos)
print('Tiempo: {} segundos'.format(time.time() - inicio))

import numpy as np

puntos = np.random.normal(loc=500,scale=30,size=10000000)
puntos

while  puntos < 500000:
    suma = suma + puntos
    print(suma)
