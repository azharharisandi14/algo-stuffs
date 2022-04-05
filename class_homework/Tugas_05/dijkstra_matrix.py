def dijkstra(g):
    
    parents = {node:None for node in len(g)}
    dist = {node:float('inf') for node in len(g)}
    unvisited = [node for node in len(g)]

    dist[0] = 0
    current = 0
    unvisited.remove(current)

    while len(unvisited) > 0:

        minnode = None
        minval = float('inf')

        # loop untuk semua neighbor
        for i, node in enumerate(g[current]):

            # jika unvisited and no inf (there is a connection)
            if i in unvisited and node != float('inf'):

                new_dist = g[current][i] + dist[current]

                # jika jarak lewat current node
                # lebih kecil dari yang sudah ada
                if new_dist < dist[i]:
                    # update parent
                    parents[i] = current

                    # update jarak
                    dist[i] = new_dist

                if new_dist < minval:
                    minnode = node
                    minval = new_dist

        # kalau ada elemen yang belum divisit
        if minval < float('inf'):
            current = minnode
            unvisited.remove(current)


        # kalau semua udah divisit
        else:
            current = unvisited.pop()

    return parents, dist


inf = float('inf')


import numpy as np 
from scipy.sparse.csgraph import shortest_path

def get_path(Pr, i, j):
    path = [j]
    k = j 
    while Pr[i,k] != -9999:
        path.append(Pr[i,k])
        k = Pr[i,k]
    return path[::-1]

M = np.array([[ 0,  7,  9,  0, 0, 14],
              [ 7,  0, 10, 15, 0,  0],
              [ 9, 10,  0, 11, 0,  2],
              [ 0, 15, 11,  0, 6,  0],
              [ 0,  0,  0,  6, 0,  9],
              [14,  0,  2,  0, 9,  0]])

D, Pr = shortest_path(M, directed=False, method='D', return_predecessors=True)

print(get_path(Pr, 0, 4))

            
            
