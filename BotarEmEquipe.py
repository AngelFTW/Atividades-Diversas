Equipe1=[]
Equipe2=[]
Equipe3=[]
Equipe4=[]
alunos=[]

while True:
  if len(alunos)>12:
    print("Todas as equipes ja foram formadas!\n")
    break
  alunoNovo=input("Digite seu nome para lhe colocar em uma equipe:\n")
  alunos.append(alunoNovo)
for aluno in alunos:
  if len(Equipe1)<3:
    Equipe1.append(aluno)
  elif len(Equipe2)<3:
    Equipe2.append(aluno)
  elif len(Equipe3)<3:
    Equipe3.append(aluno)  
  elif len(Equipe4)<3:
    Equipe4.append(aluno)

print(Equipe1)
print(Equipe2)
print(Equipe3)
print(Equipe4)