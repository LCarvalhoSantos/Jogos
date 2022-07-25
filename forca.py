import random

def jogar():
    #abertura do jogo
    abertura()
    #seleciona uma palavra secreta do arquivo txt
    palavra_sec = palavra_secreta()

    letras_acertadas = letras_certas(palavra_sec)
    
    word = letras_certas(palavra_sec)

    print("Palavra secreta meu nobre: {}".format(word))

    verifica = False
    line = "_"
    erro = 0
    tent = 5

#verificação da saida do laço
    while verifica == False :

        chute = pede_chute() 
        
        if chute in palavra_sec:
            pos = 0
            #verificando letra por letra e substituindo os underlines
            for letra in palavra_sec:
                if chute == letra:
                    word[pos] = chute
                pos = pos + 1
            print(word)
            #saída do laço em caso de acerto
            if line not in word:
                venceu(verifica)
                verifica = True
        else:
            erro += 1
            tent -= 1
            print("Você errou {} vezes. Restam {} tentativas. ".format(erro, tent))
            if erro == 5:
                #saída do laço em caso de acerto
                perdeu(verifica)
                verifica = True
        
def abertura():
    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca! :)")
    print("-----------------------------")

def palavra_secreta():    
    palavras = []
    frut_aleat = random.randint(1,12)
    frutas = open("frutas.txt","r")
    
    for linha in frutas:
        linha = linha.strip()
        palavras.append(linha)

    frutas.close()

    #list comprehentions
    palavra = palavras[frut_aleat].upper()
    return palavra
    
def letras_certas(palavra_sec):
    return ["_" for letra in palavra_sec]

def pede_chute():
    chute = input("Digite uma letra: ").upper().strip()
    return chute

def venceu(verifica):
    print("Parabéns você acertou!")

def perdeu(verifica):
    print("Infelizmente você perdeu, na próxima você consegue!!! :) ")

#iniciando jogo ao chamar arquivo forca
if __name__ == "__main__":
    jogar()
