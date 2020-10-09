"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        --> creates empty set at vertex_id in the vertices {}
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        --> from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set() # (1a)
        q.enqueue(starting_vertex)  # (1)
        
        while q.size() > 0:
            v = q.dequeue() 
            if v not in visited: # (2a)
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v): # (2b)
                    q.enqueue(neighbor)

        # ---------> [bft_NOTES] <---------
        # Breadth First Traversal
        # (1)   Init the queue [q] with the [starting_vertex] passed in
        #       --> we are using a pre-built Queue()
        #       --> SEE: projects>>graph>>[util.py]
        #       --> WHY?
        #           --> it ensures we search one level at a time
        #           --> first-in, first-out
        #           --> more details ⬇️
        #           --> guided>>2201-graphs>>README>>recorded lecture
        # (1a)  we will need a [visited] set
        #       --> keep track of where we have been
		# (2)   While our queue isn't empty ...
        #       --> take a look at front of queue
        # (2a)  if [v] has not been visited ... 
        #       --> visit the node : [print(v)]
        #       --> add v to the visited set : [visited.add(v)]
        # (2b)  enqueue all of neighbors of this node
        #       --> get all the neighbors : [self.get_neighbors(v)]
        #       --> loop thru each and add to queue : [q.enqueue(neighbor)]


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        visited = set() # (1a)
        q.push(starting_vertex) # (1)
        while q.size() > 0: # (2)
            v = q.pop()
            if v not in visited: # (2a)
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v): # (2b)
                    q.push(neighbor)

        # ---------> [dft_NOTES] <---------
        # Depth First Traversal
        # (1)   Init the stack [q] with the [starting_vertex] passed in
        #       --> push [starting_vertex] onto our stack [q]
        #       --> we are using a pre-built Stack()
        #       --> SEE: projects>>graph>>[util.py]
        #       --> WHY?
        #           --> allows us to back up and try other paths
        #           --> more details ⬇️
        #           --> guided>>2201-graphs>>README>>recorded lecture
        # (1a)  we will need a [visited] set
        #       --> keep track of where we have been
		# (2)   While our queue isn't empty ...
        #       --> look at front of the stack : [v = q.pop()]
        # (2a)  if [v] has not been visited ...
        #       --> visit the node : we will just [print(v)]
        #       --> add v to the visited set : [visited.add(v)]
        # (2b)  add all neighbors of this node to the stack
        #       --> get all the neighbors : [self.get_neighbors(v)]
        #       --> loop thru each and push onto stack

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None: # will only be true the first time around
            visited = set()  # create a visited set
        
        print(starting_vertex) # visit the node
        visited.add(starting_vertex) # add to visited set

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        # get all the neighbors for this node & loop thru each
        #   if a neighbor has not been visited ...
        #   --> recursively call [dft_recursive()] on that neighbor
        #   --> pass he new starting vertex aka [neighbor]
        #   --> pass the [visited] array so the new call has it

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()

            v = path[-1]  # v is last element in path
            
            if v not in visited:  # if v has not been visited
                if v == destination_vertex: # BASE_CASE: if last in path is the destination vertex, return the path
                    return path  # !FOUND!
                visited.add(v)  # make record that v has been visited
                # keep looking
                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)
                # get all the neighbors for this node & loop thru each
                #   create a new path to look at including this neighbor
                #   --> concat [neighbor] to [path] and save it [new_path]
                #   enqueue the new path to our queue 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]
        print(starting_vertex)
        visited.add(starting_vertex)
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                	return dfs_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('-- VERT --')
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('-- BFT --')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('-- DFT --')
    graph.dft(1)
    print('-- DFT_REC--')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('-- BFS --')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print('-- DFS --')
    # print(graph.dfs(1, 6))
    print('-- DFS_REC --')
    print(graph.dfs_recursive(1, 6))
