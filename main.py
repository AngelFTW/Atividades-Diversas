linha = input().split(" ")

X = int(linha[0])
Y = int(linha[1])

if X > Y:
    print("Decrescente")
elif X < Y:
    print("Crescente")
else:
    print(" ")
