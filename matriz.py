matriz = [ [3,2,4],[5,7,4],[9,8,7] ]

print(matriz[0][2])
print(matriz[1][2])
print(matriz[2][2])
--------------------------------------
matriz = [[1,2,3],[4,1,2],[5,9,6]]

for i in matriz:
    for j in i:
        print(j, end=' ')
    print("\n")
