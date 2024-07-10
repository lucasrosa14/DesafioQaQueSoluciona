def countingValleys(path):
    level = 0  # Nível do mar
    valleys = 0
    in_valley = False
    
    for step in path:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
        
        # Checa se entramos em um vale
        if level < 0 and not in_valley:
            valleys += 1
            in_valley = True
        
        # Checa se saímos de um vale
        if level >= 0 and in_valley:
            in_valley = False
    
    return valleys


path = "DDUUDDUDUUUD"
print('Iniciando a caminhada. \nVocê atravessou ' + str(countingValleys(path)) + ' vales.\nFinalizando a caminhada.\n ------------------')  # Saída Esperada: 2

path = "UDUUUDUDDD"
print('Iniciando a caminhada. \nVocê atravessou ' + str(countingValleys(path)) + ' vales.\nFinalizando a caminhada.\n ------------------') # Saída Esperada: 0

path = "DUDUDUDUDUDUDU"
print('Iniciando a caminhada. \nVocê atravessou ' + str(countingValleys(path)) + ' vales.\nFinalizando a caminhada.\n ------------------') # Saída Esperada: 7

path = "DDUUUUDDDUUUDDDU"
print('Iniciando a caminhada. \nVocê atravessou ' + str(countingValleys(path)) + ' vales.\nFinalizando a caminhada.\n ------------------') # Saída Esperada: 3


