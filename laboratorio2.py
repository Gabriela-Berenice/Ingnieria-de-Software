
for i in range(500,10000000,30):
    puntos = i
lista_puntos = puntos[puntos < 500000]
suma_total = np.sum(lista_puntos)

print(suma_total)
