def primo(n):
    cont = 0

    for i in range (1,10,1):
        if n % i == 0:
            cont += 1
    if n < 10:
        if cont == 2:
            return True
        else:
            return False
    else:
        if cont == 1:
            return True
        else:
            return False
        
def maior_primo(a):
    
    if a < 2:
        print("escreva um número maior ou igual a 2.")
    else:    
        while primo(a) == False:
            a -= 1

        return a

