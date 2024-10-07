coluna = 1
linha = 1
while coluna <= 10:
    while linha <= 10:
        print (linha * coluna, end='\t')
        linha += 1
    coluna += 1
    linha = 1
    print()
