import random

#TESTANDO FOR

#numero = int(input("Numero: "))
#for tabuada in range(1,11):
#    print(tabuada * numero)

#TENSTANDO F STRING

#nome = "Lucas"
#print(f"Meu nome é {nome.upper()}")

#salario='5400.5'
#print(type(salario))

#nome="Python"
#empresa='FIAP'
#qtde_funcionarios=100
#mediaMensalidade=1050.5

#total = qtde_funcionarios + mediaMensalidade

#print (total + qtde_funcionarios + nome)



#inteiros = [1,3,4,5,7,8,9]
#pares = [x for x in inteiros if x % 2 == 0]
#print(pares)

#for numero in inteiros:
#    if numero % 2 == 0:
#        pares.append(numero)

#frutas = open("frutas.txt", "w")
#frutas.write("maça\n")
#frutas.close()

#frutas = open("frutas.txt", "r")
#print(frutas.read())
#frutas.close()

frut_aleat = 0
frut_aleat = random.randint(1,12)
print(frut_aleat)

for linha in frutas:
        if linha == frut_aleat:
            palavra = frutas.readline().strip()
    print(palavra)
    word = ["_" for letra in palavra]