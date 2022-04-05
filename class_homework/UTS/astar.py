import math
import matplotlib.pyplot as plt
from collections import deque
from pprint import pprint

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g = float('inf')
        self.h = float('inf')
        self.f = self.g + self.h
        self.parent = None
        self.visited = False

    def __repr__(self):
        return f'node in row {self.row}, col {self.col}'

def manhattan(sr, sc, er, ec):
    return 10*int((abs(sr-er) + abs(sc-ec))) 

def euclidean(sr, sc, er, ec):
    return 10*int((math.sqrt((sr-er)**2 + (sc-ec)**2)))

def diagonal(sr, sc, er, ec):
    return 10*int((max(abs(sr-er), abs(sc-ec))))

def get_heuristics(heuristics):
    if heuristics == 'manhattan':
        dr = [-1, +1, 0, 0]
        dc = [0, 0, +1, -1]
        dist = [10, 10, 10, 10]

    elif heuristics == 'diagonal':
        dr = [-1, +1, 0, 0, -1, +1, +1, -1]
        dc = [0, 0, +1, -1, +1, +1, -1, -1]
        dist = [10, 10, 10, 10, 10, 10, 10, 10]

    elif heuristics == 'euclidean':
        dr = [-1, +1, 0, 0, -1, +1, +1, -1]
        dc = [0, 0, +1, -1, +1, +1, -1, -1]
        dist = [10, 10, 10, 10, 14, 14, 14, 14]
    return dr, dc, dist

def reconstruct_path(n, er, ec):
    # snode = n[sr][sc]
    enode = n[er][ec]

    path = f'){enode.col}, {enode.row}('
    while enode.parent is not None:
        path += f' >- ){enode.parent.col},{enode.parent.row}( '
        enode = enode.parent
    return path[::-1]

def get_path(n, sr, sc, er, ec):
    enode = n[er][ec]
    rows = []
    cols = []
    rows.append(enode.row)
    cols.append(enode.col)
    while enode.parent is not None:
        rows.append(enode.parent.row)
        cols.append(enode.parent.col)
        enode = enode.parent
    return rows, cols

def print_path(n, sr, sc, er, ec):
    empty = []
    for i in range(len(n)):
        empty.append([])
        for j in range(len(n[0])):
            if maze[i][j] == -1:
                empty[i].append('#')
            else:
                empty[i].append('.')
                
    
    rows, cols = get_path(n, sr, sc, er, ec)
    
    for r, c in zip(rows, cols):
        empty[r][c] = '@'
    
    empty[sr][sc] = 'S'
    empty[er][ec] = 'E'
    pprint(empty)

def plot_path(n, sr, sc, er, ec, title, **kwargs):
    empty = []
    for i in range(len(n)):
        empty.append([])
        for j in range(len(n[0])):
            if maze[i][j] == -1:
                empty[i].append(-1)
            else:
                empty[i].append(0)
                
    rows, cols = get_path(n, sr, sc, er, ec)

    for r, c in zip(rows, cols):
        empty[r][c] = 1
    
    empty[sr][sc] = 2
    empty[er][ec] = 4

    plt.imshow(empty, extent=(0, len(n[0]), 0, len(n)), **kwargs)
    plt.grid(color='w', linewidth=2)
    plt.title(title)

def a_star_search(maze, sr, sc, er, ec, heuristics):
    R = len(maze)
    C = len(maze[0])

    # start row (sr), start col (st)
    # end row (er), end col (ec)

    # grid that will contain node as its elements
    n = []
    for r in range(R):
        n.append([])
        for c in range(C):
            n[r].append(Node(r, c))

    n[sr][sc].g = 0

    node_q = deque()
    node_q.append(n[sr][sc])
    # curr = n[sr][sc]
    while len(node_q) > 0:
        curr = node_q.popleft()
        curr.visited = True

        dr, dc, dist = get_heuristics(heuristics)
        minq = {} # priority queue / min queue
        for i in range(len(dr)):
            # next row (nr) and next column (nc)
            fr = curr.row + dr[i]
            fc = curr.col + dc[i]

            if fr < 0 or fc < 0: continue
            if fr >= R or  fc >= C: continue

            if n[fr][fc].visited: continue
            if maze[fr][fc] == -1: continue

            frontier = n[fr][fc]
            # distance to starting node
            g = curr.g + dist[i]


            # distance to end node 

            if heuristics == 'euclidean':
                h = euclidean(frontier.row, frontier.col, 
                            n[er][ec].row, n[er][ec].col)
            elif heuristics == 'manhattan':
                h = manhattan(frontier.row, frontier.col, 
                            n[er][ec].row, n[er][ec].col)
            elif heuristics == 'diagonal':
                h = diagonal(frontier.row, frontier.col, 
                            n[er][ec].row, n[er][ec].col)

            if g < frontier.g:
                frontier.g = g
                frontier.h = h
                frontier.f = g+h
                frontier.parent = curr

            minq[i] = frontier
        
        if len(minq) == 0:
            break
            
        
        # sort min queue by f value
        sorted_f_minq = sorted(minq.items(), key=lambda x:x[1].f)

        if len(sorted_f_minq) > 1:
            if sorted_f_minq[0][1].f == sorted_f_minq[1][1].f:
                sorted_h_minq = sorted(minq.items(), key=lambda x:x[1].h)
                next_node = sorted_h_minq[0][1]

            else:
                next_node = sorted_f_minq[0][1]
        
        else:
            next_node = sorted_f_minq[0][1]

        node_q.append(next_node)
        
    return n



if __name__ == '__main__':

    maze = [[0, 0, -1, 0, 0, 0, 0, -1, 0, -1],
            [-1, -1, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, -1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
            [0, -1, -1, -1, -1, 0, 0, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, -1, -1, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, -1, 0, 0],
            [0, -1, 0, 0, -1, -1, -1, 0, -1, 0]]

    # starting row and column
    sr, sc = 2, 1

    # end row and column
    er, ec = 8, 9
    
    n_manhattan = a_star_search(maze, sr, sc, er, ec, 'manhattan')
    print('manhattan')
    print_path(n_manhattan, sr, sc, er, ec)

    n_diagonal = a_star_search(maze, sr, sc, er, ec, 'diagonal')
    print('diagonal')
    print_path(n_diagonal, sr, sc, er, ec)
    print('')

    n_euclidean = a_star_search(maze, sr, sc, er, ec, 'euclidean')
    print('euclidean')
    print_path(n_euclidean, sr, sc, er, ec)
    print('')

    cmap = plt.get_cmap('nipy_spectral', 5)

    plt.figure()
    plot_path(n_manhattan, sr, sc, er, ec, title='manhattan', cmap=cmap)

    plt.figure()
    plot_path(n_diagonal, sr, sc, er, ec, title='diagonal', cmap=cmap)

    plt.figure()
    plot_path(n_euclidean, sr, sc, er, ec, title='euclidean', cmap=cmap)
    
    plt.show()

