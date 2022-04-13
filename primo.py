num = int(input())

for x in range(2,num):
  if (num%x==0):
    print("nao eh primo")
    break

if(x==num-1):
  print("eh primo")