# n = número de peças inicial
# m = número máximo de peças que é possível retirar em uma rodada.

# Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador
# a iniciar a partida com a frase "Você começa!"

# Caso contrário, o computador toma a iniciativa de começar o jogo, declarando
# "Computador começa!"

escolha = 0
rodada = 0
voce = 0
computador = 0

def computador_escolhe_jogada(n,m):
    if n >= m + 1 :
        jogada = n%(m+1)
    if n <= m:
        jogada = n
    if jogada < 1:
        jogada = 1
    #print jogada
    if jogada == 1:
        print("\nO computador tirou uma peça.")
    else:
        print("\nO computador tirou",jogada,"peças.")
    return jogada


def usuario_escolhe_jogada(n,m):
    while True:
        jogada = int(input("\nQuantas peças você vai tirar? "))

        if jogada == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou",jogada,"peças.")
        
        if jogada <= m and jogada > 0:
            return jogada
            break
        else:
            print("\nOops! Jogada inválida! Tente de novo.")
        
        
    


def calcula_jogada(n, jogada):
    n = n - jogada
    if n == 0:
        return n
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam",n,"peças no tabuleiro.")
    return n 

def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    global computador
    global voce

    if n % (m+1) == 0:
        print("\nVocê começa!")
        comeca = True
    else:
        print("\nComputador começa!")
        comeca = False
        
    while n > 0:
        if comeca == True:
            jogada = usuario_escolhe_jogada(n,m)
            n = calcula_jogada(n,jogada)
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                voce += 1
                break 
            jogada = computador_escolhe_jogada(n,m)
            n = calcula_jogada(n,jogada)
            if n == 0:
                print("Fim do jogo! O Computador ganhou!")
                computador += 1
                break 
        else:
            jogada = computador_escolhe_jogada(n,m)
            n = calcula_jogada(n,jogada)
            if n == 0:
                print("Fim do jogo! O Computador ganhou!")
                computador += 1
                break 
            jogada = usuario_escolhe_jogada(n,m)
            n = calcula_jogada(n,jogada)
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                voce += 1
                break 

#main_program:
while escolha != 1 and escolha != 2:
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    print("\n1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input("> "))

    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!")
        rodada = 1
    if escolha == 2:
        print("\nVocê escolheu um campeonato!")
        rodada = 3
    if escolha != 1 and escolha != 2:
        print("\nEscolha inválida! Tente novamente!")

for rodada in range (1,rodada +1,1):

    print("\n*** Rodada",rodada,"****")

    partida()

if escolha == 2:

    print("\n**** Final do campeonato! ****")

    print("\nPlacar: Você",voce,"X",computador,"Computador")

    
    
