# Creating a Graph using Adjacency List representation
class GraphAdjList:
    def __init__(self):
        # A dictionary where key = node and value = list of connected nodes
        self.graph = {}

    def add_vertex(self, vertex):
        # Add vertex only if it doesn't already exist
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        # Add edge from u to v (undirected graph)
        
        # If 'u' is not present, create it
        if u not in self.graph:
            self.graph[u] = []
        
        # If 'v' is not present, create it
        if v not in self.graph:
            self.graph[v] = []
        
        # Add v to adjacency list of u
        self.graph[u].append(v)
        
        # Add u to adjacency list of v
        self.graph[v].append(u)

    def display(self):
        # Print graph in adjacency list form
        for vertex in self.graph:
            print(vertex, "→", self.graph[vertex])


# Example Usage
g = GraphAdjList()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.display()
