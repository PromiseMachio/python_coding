from collections import deque
graph = {
    'A':['B', 'C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C', 'E']
    }
#Dfs using recrsion
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end = " ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
    return visited
print("DFS Traversal starting from A:")
print(dfs(graph, 'A'))
print("\n")

#Bfs using queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:vertex = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        print(vertex,end = " ")
        queue.extend([n for n in graph[vertex] if n in visited])
print()
print('Bfs Traversal satrtin from A:')
print(bfs(graph, 'A'))
