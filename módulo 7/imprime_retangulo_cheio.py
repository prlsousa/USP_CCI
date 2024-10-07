l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
largura = l
while a > 0:
    while largura > 0:
        print("#", end="")
        largura -= 1
    a -= 1
    largura = l
    print()
      
