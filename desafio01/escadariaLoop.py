
while True:

    entrada = input('Digite a quantidade de degraus ou x para sair:')

    if entrada == 'x':
        print("Encerrando o programa...")
        break

    try:
        qtDegraus = int(entrada)
        def imprimeEscada():
            print('Construindo a escada...')
            for i in range(1, qtDegraus + 1):
             degrau = ('#' * i).rjust(qtDegraus)  
             print(degrau)

        imprimeEscada()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido ou x para sair.")
