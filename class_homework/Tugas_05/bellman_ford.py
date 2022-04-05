def bellman_ford(g, start):
    distance = {node:float('inf') for node in g.keys()}
    parent = {node:None for node in g.keys()}
    distance[start] = 0
    # current = start

    iter_n_result = None

    for _ in range(len(g)-1):
        all_nodes = [node for node in g.keys()]
        for node in all_nodes:
            if distance[node] != float('inf'):
                for child in g[node]:
                    new_dist = distance[node]+g[node][child]
                    if new_dist < distance[child]:
                        parent[child] = node
                        distance[child] = new_dist


        # check if there is an update from previous weight
        if iter_n_result == distance:
            break
        else:
            iter_n_result = distance

    return parent, distance

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
    'A' : {'C':-2, 'B':6},
    'B' : {'E':1},
    'C' : {'D':3},
    'D' : {'E':4},
    'E' : {},
    'F' : {'E':-5}
    }

    source = 'S'
    end = 'B'

    # run bellman_ford algorithm
    parents, distance = bellman_ford(g, source)

    # get path from start to end
    path = get_path(end, parents)
    
    print(f'path from {source} to {end} is : {path}')
    print(f'shortest distance from {source} to {end} is : {distance[end]}')