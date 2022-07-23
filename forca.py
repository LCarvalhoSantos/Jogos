from gettext import find

def jogar():

    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca! :)")
    print("-----------------------------")

    palavra = "banana".upper()
    #list comprehentions
    word = ["_" for letra in palavra]
    
    erro = int(0)
    tent = int(5)
    line = ("_")
    verifica = False
    
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