import math

def squares(a, b):
    # Encontrar o menor inteiro n tal que n^2 >= a
    n = math.ceil(math.sqrt(a))
    
    # Encontrar o maior inteiro m tal que m^2 <= b
    m = math.floor(math.sqrt(b))
    
    # Inicializar uma lista para armazenar os quadrados perfeitos
    perfect_squares = []
    
    # Coletar todos os quadrados perfeitos entre n^2 e m^2 inclusivos
    for i in range(n, m + 1):
        perfect_squares.append(i * i)
    
    # Imprimir o array de quadrados perfeitos
    print(perfect_squares)
    
    # Retornar o número de quadrados perfeitos
    return len(perfect_squares)

# Exemplos de teste
print(squares(3, 9))  # Saída esperada: 2
print(squares(24, 49))  # Saída esperada: 3
print(squares(17, 24))  # Saída esperada: 0
print(squares(35, 70))  # Saída esperada: 3
print(squares(100, 1000))  # Saída esperada: 22
print(squares(59, 999999922))  # Saída esperada: 31615
print(squares(9, 999999966))  # Saída esperada: 31620
print(squares(12, 999999988))  # Saída esperada: 31619
