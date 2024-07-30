import heapq

def shortestReach(n, edges, s):
    # Cria uma lista de adjacências
    graph = [[] for _ in range(n + 1)]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Inicializa as distâncias e a fila de prioridade
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    priority_queue = [(0, s)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(priority_queue, (distance, v))
    
    # Prepara o resultado final ignorando o nó inicial e os inatingíveis
    result = []
    for i in range(1, n + 1):
        if i == s:
            continue
        if dist[i] == float('inf'):
            result.append(-1)
        else:
            result.append(dist[i])
    
    return result

# Exemplos de testes
print(shortestReach(4, [(1, 2, 24), (1, 4, 20), (3, 1, 3), (4, 3, 12)], 1))  # Output: [24, 3, 15]
print(shortestReach(5, [(1, 2, 10), (1, 3, 6), (2, 4, 8)], 2))  # Output: [10, 16, 8, -1]
print(shortestReach(6, [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 4, 11), (3, 6, 2), (4, 5, 6), (5, 6, 9)], 1))  # Output: [7, 9, 20, 20, 11]
print(shortestReach(3, [(1, 2, 1), (2, 3, 1)], 1))  # Output: [1, 2]
print(shortestReach(4, [(1, 2, 1), (2, 3, 2), (3, 4, 3)], 2))  # Output: [1, 2, 5]
