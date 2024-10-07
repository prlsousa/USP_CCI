n = int(input("Digite um número inteiro: "))
digito_anterior = 10
soma = 0 
while n != 0:
    digito = n % 10
    n = n // 10
    if digito == digito_anterior:
        soma += 1
    digito_anterior = digito

if soma != 0:
    print("sim")
else:
    print("não")
