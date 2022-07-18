import random

print("Bem-vindo ao jogo de advinhação! :)")

num_secret = random.randint(1, 100)
chute = 0
cont = 0

#repetindo caso o usuário erre o número secreto
while (chute != num_secret):
    cont = cont + 1
    chute = int(input("Digite um número de 1 - 100: "))
    if(chute <= 100 or chute <= 0):
#realizando o teste do chute na estrutura de decisão
        if (chute > num_secret):
            print("******************************************\n")
            print("Número digitado: {}". format(chute))
            print("Tente um numero menor.")
            print("Total de tentativas: {} ".format(cont), "\n")
            print("******************************************")
        elif chute < num_secret:
            print("******************************************\n")
            print("Tente um numero maior!")
            print("Total de tentativas: {} ".format(cont), "\n")
            print("******************************************")
        else:
            print("******************************************\n")
            print("Você acertou!!!")
            print("Total de tentativas: {} ".format(cont), "\n")
            print("******************************************")
    else:
        print("Digite um número válido")
