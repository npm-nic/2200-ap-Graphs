islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

islands_2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# copypasta from by Beej
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def island_counter(islands):
    visited = set() # (2a)
    counter = 0 # (2a)

    # needed for bft()
    def get_neighbors(coords):

        neighbors = []

        row, col = coords
        if row > 0 and islands[row-1][col] == 1:
            neighbors.append((row-1, col))
        if row < len(islands) - 1 and islands[row+1][col] == 1:
            neighbors.append((row+1, col))
        if col > 0 and islands[row][col-1] == 1:
            neighbors.append((row, col-1))
        if col < len(islands[row]) - 1 and islands[row][col+1] == 1:
            neighbors.append((row, col+1))
        return neighbors
        ''' -----> get_neighbors_NOTES <-----'''
        # neighbors checked:
        #       previous row      [row-1]
        #       next row          [row+1]
        #       previous column   [col-1]
        #       next column       [col+1]
        # edge cases checked:
        # --> don't check rows or columns that don't exist
        #       row > 0
        #       row < (length of islands -1)
        #       col > 0
        #       col < (length of island[rows] - 1)

    # standard bft()
    def bft(row, col):
        q = Queue()
        q.enqueue((row, col)) 

        while q.size() > 0:
            coords = q.dequeue()
            if coords not in visited:
                visited.add(coords)
                for neighbor in get_neighbors(coords):
                    q.enqueue(neighbor)
    
    for row in range(len(islands)): # (1)
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            coords = (row, col) # (1a)

            if coords not in visited and node_val == 1: # (2)
                bft(row, col) # (2a)
                counter += 1 # (2a)
    return counter  # (3)
    
    ''' ---------> island_counter_NOTES <---------'''
    # (1)   for all the nodes in the graph
    #       --> ASSUMED: all lengths of row are equal
    #       --> we are getting the row & col for each of these nodes
    #           --> this allows us to look up the node values
    # (1a)  creating a ~tuple~ so that we can look up coordinates / values

    # (2)   if we find an unvisited '1' node:
    # (2a)  BFT from that node
    #       --> visited declared outside of btf() because you want it to persist each traversal (call-to-call)
    # (2b)  increment our [counter]
    # (3)   return our [counter]


''' test zone
    ______________________
    ...ctrl `...
    cd guided/2203-graphs
    python3 islands.py
    ______________________

'''
print(island_counter(islands)) # returns 4
print(island_counter(islands_2)) # returns 13 
