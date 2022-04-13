def castelo():
  print("\nNo castelo a princesa te serve com um banquete e conta para o rei que você a salvou, ele decide te normear um cavaleiro real, você aceita?\n")
  if input() == "sim":
    print ("\nVocê se torna um cavaleiro real e se casa com a princesa\n")
    print ("\nParabéns, você venceu o jogo\n")
  if "nao":
    print("\nVocê decide ficar um tempo no castelo\n")


def dormir():
  print("\nVocê dormiu e acorda com suas energias cheias e magicamente\nacorda na fogueira inicial\n")
  return chamarMenu()


def chamarMenu():
  menu = input("Você começa sentado numa fogueira\nexistem quatro direções para ir, norte/sul/leste/oeste, para onde deseja ir?\n\n")
  if (menu == "leste"):
    print("Você avista um aldeia, deseja seguir em direção à ela?")
    if input() == "sim":
      print("\nVocê não fala a língua dos aldeões e volta para a fogueira\n\n")

      return chamarMenu()
    else:
    
      return chamarMenu()
  if (menu == "norte"):
    print("\nEstá muito frio mas você vê uma caverna, deseja entrar na caverna ou seguir?(Digite caverna ou seguir)\n\n")
    if input() == "seguir":
      print("\nVocê morreu de frio\n\n") 
      return chamarMenu()
    if "caverna":
      print("\nVocê acha algumas frutas, come e fica sonolento\n")
      return dormir()

  if (menu == "sul"):
    print ("\nVocê avista uma dama sendo atacada por um lobo, deseja salva-la?\n")
    if input() == "sim":
      print("\nVocê consegue salva-lá e ela te leva\npro castelo dela para te recompensar\n")
      return castelo()
    else:
       print("Ela morre e o lobo vai em sua direção")

  if (menu == "leste"):
    print("\nEstá muito frio mas você vê uma caverna, deseja entrar na caverna ou seguir?(Digite caverna ou seguir)\n\n")



chamarMenu()