n=[]
n.append(int(input("Digite um número inteiro, digite 0 quando quiser terminar: ")))
i = 0
while n[i] != 0:
    n.append(int(input("Digite outro número inteiro, digite 0 quando quiser terminar: ")))
    i += 1
del(n[i])
max = len(n)-1

while max >= 0:
    print(n[max],end="\n")
    max -= 1
