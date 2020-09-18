import numpy as np
import time 

# abri docuemnto txt y guardar en una variable
with open('costos.txt') as c:
    lista_costos = c.read().split('\n')

inicio = time.time()
menor = []

#convertir a int la lista txt
costos = map(int, lista_costos)

#comparacion de los numeros iguales o menores a 25
for valor in costos:
    if valor <= 25:
        menor.append(valor)
        monto_total = np.sum(menor)

#imprimir gasto total y el tiempo
print('Monto total de seleccion es $', monto_total)
print('Tiempo: {} segundos'.format(time.time() - inicio))
