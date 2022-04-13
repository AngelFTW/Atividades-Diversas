from random import randint
Matriz = []*10

for i in range(0,10):
    linha = []
    for j in range(0,3):
        elemento = randint(0, 9)
        linha.append(elemento)
    Matriz.append(linha)
print(Matriz)