import random
    
def jogar():    
    print("------------------------------------")
    print("Bem-vindo ao jogo de advinhação! :)")
    print("------------------------------------")

    num_secret = random.randint(1, 100)
    chute = 0
    cont = 0
    pontos = int(1000)

    #repetindo caso o usuário erre o número secreto
    while (chute != num_secret):
        cont = cont + 1
        chute = int(input("Digite um número de 1 - 100: "))
        if(chute > 0 or chute < 101):
    #realizando o teste do chute na estrutura de decisão
            if (chute > num_secret):
    #criando pontuação
                pontos = pontos - (abs(chute - num_secret))
                print(pontos)
                print("******************************************\n")
                print("Número digitado: {}". format(chute))
                print("Tente um numero menor. Pontuação atual é de {} pontos".format(pontos))
                print("Total de tentativas: {} ".format(cont), "\n")
                print("******************************************")
            elif chute < num_secret:
                pontos = pontos - (abs(chute - num_secret))
                print("******************************************\n")
                print("Número digitado: {}". format(chute))
                print("Tente um numero maior. Pontuação atual é de {} pontos".format(pontos))
                print("Total de tentativas: {} ".format(cont), "\n")
                print("******************************************")
            else:
                print("******************************************\n")
                print("Você acertou!!! Pontuação atual é de {} pontos".format(pontos))
                print("Total de tentativas: {} ".format(cont), "\n")
                print("******************************************")
        else:
            print("Digite um número válido")

#iniciando jogo ao executar arquivo adivinhacao
if __name__ == "__main__":
    jogar()