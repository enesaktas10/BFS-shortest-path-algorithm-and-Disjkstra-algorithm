import heapq


graph = {
    'A': {'B': 4, 'C': 2, 'E': 7},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 4, 'E': 8},
    'D': {'B': 5, 'C': 4, 'E': 3},
    'E': {'A': 7, 'C': 8, 'D': 3}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        pass
        if current_distance > distances[current_node]:
            continue
        

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  
    return distances

start_node = 'A'
result = dijkstra(graph, start_node)

print("Başlangıç noktasından diğer noktalara olan en kısa mesafeler:")
for node, distance in result.items():
    print(f"{start_node} -> {node}: Mesafe = {distance}")
