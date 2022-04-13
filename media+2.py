qtd = int(input())
media=0

for x in range(qtd):
  nota=int(input())
  media = nota+media
print(media/qtd)