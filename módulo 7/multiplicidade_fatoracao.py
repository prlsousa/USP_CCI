fator = 2
multiplicidade = 0
n = 600
while n != 1:
    while n % fator == 0:
        multiplicidade +=1
        n = n / fator
    if multiplicidade > 0:
        print("fator",fator,"multiplicidade",multiplicidade)
    fator += 1
    multiplicidade = 0
