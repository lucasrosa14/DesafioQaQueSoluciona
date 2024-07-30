import math

def encryption(s):
    # Remover espaços da string
    s = s.replace(" ", "")
    
    # Calcular o comprimento da string sem espaços
    L = len(s)
    
    # Calcular o número de linhas e colunas da grade
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    # Ajustar número de linhas e colunas para atender a condição de que a área da grade deve ser suficiente
    if rows * cols < L:
        rows += 1
    
    # Criar a grade
    grid = []
    for i in range(rows):
        grid.append(s[i * cols: (i + 1) * cols])
    
    # Construir a string criptografada lendo as colunas
    encrypted_message = []
    for c in range(cols):
        column_chars = [grid[r][c] for r in range(rows) if c < len(grid[r])]
        encrypted_message.append("".join(column_chars))
    
    return " ".join(encrypted_message)

# Testes
s = "haveaniceday"
print(encryption(s))  # Saída: "hae and via ecy"

s = "feedthedog"
print(encryption(s))  # Saída: "fto ehg ee dd"

s = "chillout"
print(encryption(s))  # Saída: "clu hlt io"

s = "iuo"
print(encryption(s))  # Saída: "io u"

s = "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"
print(encryption(s))  # Saída: "wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy"