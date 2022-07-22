from gettext import find

def jogar():

    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca! :)")
    print("-----------------------------")

    word = ["_","_","_","_","_","_"]
    palavra = "banana".upper()
    erro = int(0)
    underline = ("_")
    validacao = False

    print("Palavra secreta meu nobre: {}".format(word))

    while erro < 6 or validacao == False:
        chute = input("Digite uma letra: ").upper().strip()
        if chute in palavra:
            tamanho = int(len(word))
            pos = 0
            for letra in palavra:
                if chute == letra:
                    word[pos] = chute
                pos = pos + 1
                validacao = find("_" in word)
                print(validacao)
            print(word)
        else:
            erro = erro + 1

#iniciando jogo ao chamar arquivo forca
if __name__ == "__main__":
    jogar()