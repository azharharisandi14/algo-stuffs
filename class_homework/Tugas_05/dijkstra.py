def dijkstra(g, start):
    parents = {node:None for node in g.keys()}
    dist = {node:float('inf') for node in g.keys()}
    unvisited = [node for node in g.keys()]

    dist[start] = 0

    current = start
    unvisited.remove(start)
    while len(unvisited) > 0:
        # kalau dictionary tidak kosong
        if g[current]: 

            # variabel untuk cek neighbor mana 
            # yang jaraknya paling kecil
            minnode = None
            minval = float('inf')

            # loop untuk semua keyword
            for node in g[current]:

                # jika node masih belum divisit
                if node in unvisited:
                    # jumlah distance dari start node
                    new_dist = g[current][node] + dist[current]

                    # jika jarak lewat current node 
                    # lebih kecil dari jarak yang sudah ada
                    if  new_dist < dist[node]:
                        # update parentnya
                        parents[node] = current
                        # update jaraknya
                        dist[node] = new_dist

                    if new_dist < minval:
                        minnode = node
                        minval = new_dist                        

            # kalau ada elemen yang belum divisit
            if minval < float('inf'):
                current = minnode
                unvisited.remove(current)

            # kalau semua elemennya udah divisit
            else:
                current = unvisited.pop()

        # kalau kosong, langsung pop elemennya sembarang
        else:
            current = unvisited.pop()
            
    return parents, dist

def get_path(end, parents_dict):
    path = f'{end}'
    while parents_dict[end] is not None:
        node = parents_dict[end]
        path += f' >- {node}'
        end = node
    return path[::-1]

if __name__ == '__main__':
    g = {
    'S' : {'A':3, 'C':2, 'F':6},
    'A' : {'D':1, 'B':6},
    'B' : {'E':1},
    'C' : {'A':2, 'D':3},
    'D' : {'E':4},
    'E' : {},
    'F' : {'E':2}
    }

    g = [[0, 3, inf, 2, inf, inf, 6],
     [inf, 0, 6, inf, 1, inf, inf],
     []]
    
    source = 'S'
    end = 'E'

    # run dijkstra algorithm
    parents, distance = dijkstra(g, source)

    # get path from start to end
    path = get_path(end, parents)
    
    print(f'path from {source} to {end} is : {path}')
    print(f'shortest distance from {source} to {end} is : {distance[end]}')

