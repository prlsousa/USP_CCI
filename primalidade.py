n = int(input("Digite um número inteiro: "))

cont = 0

for i in range (1,10,1):
    if n % i == 0:
        cont += 1
if n < 10:
    if cont == 2:
        print("primo")
    else:
        print("não primo")
else:
    if cont == 1:
        print("primo")
    else:
        print("não primo")
