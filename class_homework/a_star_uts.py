from pprint import pprint
inf = float('inf')

name2idx = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
idx2name = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
h = [5, 3, 4, 2, 6, 0, 4]

parent = {0:None, 1:None, 2:None, 3:None, 
    4:None, 5:None, 6:None}

def create_uniform_list(reference_list, element):
    f = []
    for i in range(len(reference_list)):
        f.append([])
        for j in range(len(reference_list[0])):
            try:
                f[i].append(element)
            except:
                f[i].append(None)
    return f

def reconstruct_path(end, parents):
    global name2idx, idx2name
    path = f' {end} '
    end = name2idx[end]
    while end:
        path += f'>- {idx2name[parent[end]]} '
        end = parent[end]
    return path[::-1]
    
# adjacency matrix
edge = [[0, 1, 3, None, None, 10, None],
    [1, 0, 1, 7, 5, None, 2],
    [3, 1, 0, 9, 3, None, None],
    [None, 7, 9, 0, 2, 1, 12],
    [None, 5, 3, 2, 0, 2, None],
    [None, None, None, 1, 2, 0, None],
    [None, 2, None, 12, None, None, 0]]

# matrix for f value
f = create_uniform_list(edge, 0)

# matrix for g value
g = create_uniform_list(edge, inf)

# g where col == row is zero (g to itself)
for i in range(len(g)):
    for j in range(len(g[i])):
        if i == j:
            g[i][j] = 0


# start
start_node = name2idx['A']
end_node = name2idx['F']
g[start_node][start_node] = 0
queue = []
visited = []
queue.append(start_node)

while len(queue) > 0:
    curr = queue.pop()
    visited.append(curr)

    if end_node in visited:
        break

    smallest = []
    for col, node in enumerate(edge[curr]):
        if node: 
            if col not in visited:
                g_current = node + g[curr][curr]
                if g_current < g[curr][col]:
                    f_current = g_current + h[col]
                    g[curr][col] = g_current
                    g[col][curr] = g_current

                    f[curr][col] = f_current
                    f[col][curr] = f_current

                    parent[col] = curr

                smallest.append((col, f[curr][col]))
    

    if not smallest:
        break

    next_node = sorted(smallest, key=lambda x:x[1])[0]
    queue.append(next_node[0])

# print(parent)
print('f = g + h')
pprint(f)
print('')

path = reconstruct_path('F', parent)
print('Path from A to F')
print(path)



