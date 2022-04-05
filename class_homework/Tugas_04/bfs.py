# BFS

"""

visited = []

1. choose starting vertex
2. visit starting vertex (add to visited)
3. explore adjacent vertices (go to other vertex)
4. visit that other vertex (change visited to 1 for that new vertex)

"""

graph1 = {
    1 : [2, 4, 5],
    2 : [1, 3, 6, 7],
    3 : [2],
    4 : [1],
    5 : [1],
    6 : [2],
    7 : [2]
}

from collections import deque

def bfs(adjacency_list, start):
    traverse = []
    visited = {}
    level = {}
    parent = {}
    q = deque()

    for node in adjacency_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    visited[start] = True
    level[start] = 0
    q.append(start)
    
    while q:
        current = q.popleft()
        traverse.append(current)

        for vertex in adjacency_list[current]:
            if not visited[vertex]:
                visited[vertex] = True
                parent[vertex] = current
                level[vertex] = level[current] + 1
                q.append(vertex)
    
    return traverse, level, parent


traverse, level, parent = bfs(graph1, 1)
print('traverse : ', traverse)
print('level : ', level)
print('parent : ', parent)


# Shortest path from source node to any node
destination = 7
path = []
while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(f"path from 1 to 7 : ", path)


