import matplotlib.pyplot as plt

disciplinas = ['Estrutura', 'Banco de Dados', 'Arquitetura']
medias = [10, 6, 8]

plt.xlabel('Notas')
plt.ylabel('Disciplinas')
plt.plot(disciplinas, medias)
plt.show()
