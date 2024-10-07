n = 1
seq = [3, 42, 105]
max = 1
qtd_numeros = len(seq)
qtd_divisoes = 0
while n <= qtd_numeros:
    i = 0
    while i < qtd_numeros:
        if seq[i]% n == 0:
            qtd_divisoes += 1
        i += 1
        if qtd_divisoes == qtd_numeros:
            max = n
    n += 1
    qtd_divisoes = 0
print(max)
        
