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
limite = int(input("Limite máximo: "))
n = 2
while n < limite:
    if éPrimo(n):
        print(n,end=", ")
    n = n + 1
    

        
