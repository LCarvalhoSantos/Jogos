import random

print("Bem-vindo ao jogo de advinhação! :)")

num_secret = random.randint(1, 100)
chute = 0
saida = 1
cont = 0

while chute != num_secret and saida == 1:
    cont = cont + 1
    chute = int(input("Digite um número de 1 - 100: "))
    if chute > num_secret:
        print("******************************************\n")
        print("Número digitado: ", chute)
        print("Tente um numero menor.")
        print("Número de tentativas: ", cont, "\n")
        print("******************************************")
    elif chute < num_secret:
        print("******************************************\n")
        print("Tente um numero maior!")
        print("Número de tentativas: ", cont, "\n") 
        print("******************************************")
    else:
        print("******************************************\n")
        print("Você acertou!!!")
        print("Número de tentativas: ", cont, "\n")
        print("******************************************")
        saida = 0
