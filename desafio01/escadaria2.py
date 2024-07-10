
def imprimeEscada(n):
    print('Construindo a escada com ' + str(n) +' degraus...')
    print('                       ')
    for i in range(1, n + 1):
        degrau = ('#' * i).rjust(n)  
        print(degrau)


imprimeEscada(2)

imprimeEscada(7)

imprimeEscada(20)