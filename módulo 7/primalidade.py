n = int(input("Digite um número inteiro: "))

def éPrimo(x):
    fator = 1
    qtd = 0
    while fator <= x:
        if x % fator == 0:
            qtd += 1
        fator += 1
    if qtd == 2:
        return True
    else:
        return False
    
while n > 0:
    if éPrimo(n):
        print(n,"é primo")
    else:
        print(n,"não e primo")
    n = int(input("Digite um número inteiro: "))

        
