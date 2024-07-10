def beautifulDays(i, j, k):
    # Função para reverter um número
    def reverse_number(n):
        return int(str(n)[::-1])
    
    beautiful_count = 0
    
    for day in range(i, j + 1):
        reversed_day = reverse_number(day)
        difference = abs(day - reversed_day)
        
        if difference % k == 0:
            beautiful_count += 1
    
    return beautiful_count

print(beautifulDays(20, 23, 6))  # Saída: 2
print(beautifulDays(13, 45, 3))  # Saída: 33
print(beautifulDays(1, 2000000, 2000000))  # Saída: 2998
print(beautifulDays(1, 2000000, 23047885))  # Saída: 2998


