G = {
    'A' : ['B','D'],
    'B' : ['C','D','E'],
    'C' : ['B'],
    'D' : ['B'],
    'E' : ['B','F'],
    'F' : ['E','G'],
    'G' : ['F']
}

def bfs_shortest_path(graph, node1, node2):
    visited_nodes = {node1} 
    index = 0
    init_list = [[node1]]
    

    if node1 == node2:
        return init_list[0]
        
    while index < len(init_list):
        current_path = init_list[index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        for next_node in next_nodes:
            if not next_node in visited_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                init_list.append(new_path)
                visited_nodes.add(next_node)
        index += 1
    return []

result= bfs_shortest_path(G,'A','G')
print(result)
