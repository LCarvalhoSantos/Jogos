import forca
import adivinhacao

print("-----------------------------")
print("-----Escolha o seu jogo!-----")
print("-----------------------------\n")

jogo = int(input("1 - Forca | 2 - Advinhação: "))
print("-----------------------------")

if jogo == 1:
    print("-----------------------------")
    print("Abrindo jogo da Forca")
    print("-----------------------------")
    forca.jogar()
else:
    print("-----------------------------")
    print("Abrindo jogo de Advinhação")
    print("-----------------------------")
    adivinhacao.jogar()
