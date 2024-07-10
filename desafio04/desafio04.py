from bisect import insort, bisect_left

def activityNotifications(expenditure, d):
    def get_median(arr):
        n = len(arr)
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2
    
    notifications = 0
    trailing_days = sorted(expenditure[:d])
    
    for i in range(d, len(expenditure)):
        median = get_median(trailing_days)
        if expenditure[i] >= 2 * median:
            notifications += 1
        
        # Remove the element that is sliding out of the window
        old_element_index = bisect_left(trailing_days, expenditure[i - d])
        trailing_days.pop(old_element_index)
        
        # Add the new element into the window, maintaining sorted order
        insort(trailing_days, expenditure[i])
    
    return notifications

#Teste 1:
#Entrada: 
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5] 
d = 5
#Saída Esperada: 2
print(activityNotifications(expenditure, d))  

#Teste 2:
# Entrada: 
expenditure = [1, 2, 3, 4, 4] 
d = 4
# Saída Esperada: 0
print(activityNotifications(expenditure, d))  

# Teste 3:
# Entrada: 
expenditure = [10, 20, 30, 40, 50, 60, 70, 80, 90] 
d = 5
# Saída Esperada: 1
print(activityNotifications(expenditure, d))  

# Teste 4:
# Entrada: 
expenditure = [1, 2, 100, 2, 2, 2, 2, 2] 
d = 4
# Saída Esperada: 0
print(activityNotifications(expenditure, d))  