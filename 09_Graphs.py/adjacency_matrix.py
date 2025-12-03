# Graph implementation using Adjacency Matrix
class GraphAdjMatrix:
    def __init__(self, vertices):
        # Store number of vertices
        self.V = vertices
        
        # Create a V x V matrix filled with 0
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add an undirected edge: mark 1 in both directions
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def display(self):
        # Print adjacency matrix in grid form
        for row in self.matrix:
            print(row)


# Example usage with 4 nodes: 0,1,2,3
g = GraphAdjMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.display()
