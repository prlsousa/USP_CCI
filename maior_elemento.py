def maior_elemento(lista):
    maior = -10000000
    for item in lista:
        if item > maior:
            maior = item
    return maior
