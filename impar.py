from random import randint
Matriz = []

for i in range(0,5):
  linha = []
  for j in range(0,5):
    elemento = randint(0, 9)
    linha.append(elemento)
  Matriz.append(linha)


print(Matriz)

par =[]
impar=[]

for j in linha:
  if(j%2==0):
    par.append(j)
  else:
    impar.append(j)
print("Pares:",par)
print("Impares:",impar)

