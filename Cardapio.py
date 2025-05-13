opcao = 0
while opcao != 5:
    print ("Cardapio")
    print ("1- hamburguer")
    print ("2- Pizza")
    print ("3- salada")
    print ("4- refri")
    print ("5- sair")
    opcao = int(input("Escolha a opcão: "))
    if opcao ==1:
      print ("Você escolheu hamburguer.")
    elif opcao ==2:
      print ("Você escolheu pizza.")
    elif opcao ==3:
      print ("Você escolheu salada.")
    elif opcao ==4:
      print ("Você escolheu refri.")
    elif opcao ==5:
      print ("Você escolheu sair do cardapio.")
      break
    else:
      print ("Opção invalida. tente novamente.")