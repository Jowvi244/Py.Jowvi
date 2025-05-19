opcao = 0
valor_frances = 0
valor_integral = 0
valor_doce = 0
valor_farofa = 0
valor_forma = 0
while opcao !=6:
    print ("Padaria")
    
    print ("1-Pão francês:$1,04")
    print ("2-Pão integral:$1,04")
    print ("3-Pão doce liso:$1,08")
    print ("4-Pão doce farofa:$1,11")
    print ("5-Pão de forma:$0,95")
    print ("6-Para sair!!")
    opcao = int(input("Escolha a sua opção."))
    if opcao == 1:
        print ("Você escolheu pão francês.")
        quantidade_frances= int(input("Digite a quantidade: "))
        valor_frances + quantidade_frances*1.04
        
    elif opcao == 2:
        print ("Você escolheu pão integral. ")
        quantidade_integral= int(input("Digite a qauntidade: "))
        valor_integral + quantidade_integral*1.04
        
    elif opcao == 3:
        print ("você escolheu pão doce liso.")
        quantidade_doce= int(input("Digite a quantidade:"))
        valor_doce + quantidade_doce*1.08
        
    elif opcao == 4:
        print ("Você escolheu pão doce farofa.")
        quantidade_farofa= int(input("Digite a qauntidade:"))
        valor_farofa + quantidade_farofa*1.11
        
    elif opcao == 5:
        print ("Você escolheu pão de forma.")
        quantidade_forma= int(input("Digite a quantidade:"))
        valor_forma + quantidade_forma*0.95
        
    elif opcao == 6:
        print ("Você saiu do cardapio.")
        break
    else :
        print ("Opção invalida")