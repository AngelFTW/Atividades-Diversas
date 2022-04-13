fila = []

for i in range(5):
    fila.append(i)
    print(fila)

for i in range(5):
    fila.remove(i)
    print('Saiu da fila o índice {} de valor :' . format(i))
    print(fila)
