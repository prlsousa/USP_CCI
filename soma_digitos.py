n = int(input("Digite um número inteiro: "))
soma = 0
digito = 0
while n != 0:
    dígito = n % 10
    n = n // 10
    soma += dígito

print(soma)