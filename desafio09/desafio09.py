def similarity(s):
    def common_prefix_length(a, b):
        """Calcula o comprimento do prefixo comum mais longo entre as strings a e b"""
        length = 0
        min_len = min(len(a), len(b))
        for i in range(min_len):
            if a[i] == b[i]:
                length += 1
            else:
                break
        return length

    total_similarity = 0
    n = len(s)

    # Iterar sobre cada sufixo
    for i in range(n):
        sufix = s[i:]
        total_similarity += common_prefix_length(s, sufix)

    return total_similarity

# Testes
s = "ababaa"
print(similarity(s))  # Saída esperada: 11

s = "aa"
print(similarity(s))  # Saída esperada: 3

s = "abcabccba"
print(similarity(s))  # Saída esperada: 13

s = "eabdcbbeeedbdaebdedbcbdcdeeaebbdbedbdbccbaaeababba"
print(similarity(s))  # Saída esperada: 63

s = "bcdedeccaabdaebdddaeedabedccdddccbbaaadcbbabccbaadbbbeddecacddbababbabadcbbbacecdaee"
print(similarity(s))  # Saída esperada: 105

s = "aeccbdaadbcebddbadbaedeceedbcdaaadcbdebecaddedebccdbadaeed"
print(similarity(s))  # Saída esperada: 70
