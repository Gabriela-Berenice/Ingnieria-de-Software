import numpy as np
import time 

with open('costos.txt') as c:
    lista_costos = c.read().split('\n')

inicio = time.time()
menor = []

costos = map(int, lista_costos)

#comparacion de los numeros iguales o menores a 25
for valor in costos:
    if valor <= 25:
        menor.append(valor)
        monto_total = np.sum(menor)

print('Monto total de seleccion es $', monto_total)
print('Tiempo: {} segundos'.format(time.time() - inicio))
