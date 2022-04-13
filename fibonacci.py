qtd = int(input())
n1=0
n2=1

print(n1,n2)
for x in range(2,qtd):
  prox=n1+n2
  print(prox)
  n1=n2
  n2=prox