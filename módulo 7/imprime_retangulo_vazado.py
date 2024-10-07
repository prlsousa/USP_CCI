l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
largura = l
altura = a
while a > 0:
    if altura == a or a == 1:
        while largura > 0:
            print("#", end="")
            largura -= 1
    else:
        while largura > 0:
            if largura == l or largura == 1:
                print("#", end="")
            else:
                print(" ", end="")
            largura -= 1
    a -= 1
    largura = l
    print()
