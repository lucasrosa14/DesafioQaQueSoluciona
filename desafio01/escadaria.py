
print('Digite a quantidade de degraus:')
qtDegraus = int(input())

def imprimeEscada():
    print('Construindo a escada...')
    for i in range(1, qtDegraus + 1):
        degrau = ('#' * i).rjust(qtDegraus)  
        print(degrau)

imprimeEscada()
