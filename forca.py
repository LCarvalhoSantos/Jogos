import random

def jogar():

    abertura()

    palavra_secreta()



    
    print("Palavra secreta meu nobre: {}".format(word))

#verificação da saida do laço
    while verifica == False :
        chute = input("Digite uma letra: ").upper().strip()
        if chute in palavra:
            pos = 0
            #verificando letra por letra e substituindo os underlines
            for letra in palavra:
                if chute == letra:
                    word[pos] = chute
                pos = pos + 1
            print(word)
            #saída do laço em caso de acerto
            if line not in word:
                verifica = True
                print("Parabéns você acertou!")
        else:
            erro += 1
            tent -= 1
            print("Você errou {} vezes. Restam {} tentativas. ".format(erro, tent))
            if erro == 5:
                #saída do laço em caso de acerto
                verifica = True
                print("Infelizmente você perdeu, na próxima você consegue!!! :) ")
        
#iniciando jogo ao chamar arquivo forca
if __name__ == "__main__":
    jogar()



def abertura():
    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca! :)")
    print("-----------------------------")

def palavra_secreta():    
    palavras = []
    frut_aleat = 0
    frut_aleat = random.randint(1,12)
    frutas = open("frutas.txt","r")
    
    for linha in frutas:
        linha = linha.strip()
        palavras.append(linha)

    frutas.close()

    #list comprehentions
    palavra = palavras[frut_aleat].upper()
    word = ["_" for letra in palavra]

