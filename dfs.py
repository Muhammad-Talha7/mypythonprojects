graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(node, visited=None):
    if visited is None:
        visited = set()

    print(node,"->", end=' ')
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


print("DFS traversal starting from A:")
dfs('A')  
