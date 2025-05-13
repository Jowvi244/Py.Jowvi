#Declarar variaveis
import random
numero_secreto = random.randint (1,10)
tentativas =0
contagem_tentativas = 0
print ("Bem vindo ao jogo de adivinhação.")
print ("Tente adivinhar o numero secreto entre 1 a 10.:")
while tentativas != numero_secreto:
    numero = int(input("Digite um numero:"))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Parebens! você acertou *-*")
        print (f"você precisou de {contagem_tentativas}tentativas.")
        break #Parar laço de repetição 
    elif numero < numero_secreto: 
        print ("O numero secreto é maior.")
    else:
        print ("O numero secreto é menor")
