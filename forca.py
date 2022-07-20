def jogar():

    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca! :)")
    print("-----------------------------")

    palavra = "banana".upper()
    tentativas = int(0)

    while tentativas <= 5:
        chute = input("Digite uma letra: ").upper().strip()

        pos = 0
        for letra in palavra:
            if chute == letra:
                print(chute)
                palavra.find(chute)

            else:
                print("*")
            
            pos =+1
            tentativas = tentativas + 1
        

#iniciando jogo ao chamar arquivo forca
if __name__ == "__main__":
    jogar()