# A* Search (brief)

# Definition: Heuristic best-first search for shortest path from source to goal using f(n)=g(n)+h(n) where h is admissible heuristic.
# Use: When you need goal-directed search (e.g., pathfinding on maps).
# Advantage: Often much faster than Dijkstra when good heuristic exists.
# Limitation: Requires admissible/consistent heuristic; worst-case can be as slow as Dijkstra.
# Purpose of this version

# Brief implementation

# Every line fully commented

# Works on graphs represented using adjacency lists

# Uses f(n) = g(n) + h(n)

# Assumes the heuristic h(n) is admissible and consistent
import heapq  # Importing heapq for priority queue operations

def a_star(graph, start, goal, heuristic):
    """
    A* Search Algorithm
    graph     : dictionary representing adjacency list with weights
    start     : starting node
    goal      : target node we want to reach
    heuristic : admissible heuristic function h(n)
    """

    # Priority queue (min-heap) storing: (f_cost, node)
    open_set = []
    
    # Push the start node with f(start) = g(start) + h(start)
    heapq.heappush(open_set, (heuristic(start, goal), start))

    # Stores the shortest discovered distance from start to each node (g(n))
    g_cost = {start: 0}

    # To reconstruct path: child -> parent mapping
    parent = {start: None}

    # Loop until priority queue becomes empty
    while open_set:
        # Pop the node with the lowest f(n)
        current_f, current_node = heapq.heappop(open_set)

        # If goal reached → reconstruct and return path
        if current_node == goal:
            return reconstruct_path(parent, goal)

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # g(n) cost for reaching neighbor through current
            tentative_g = g_cost[current_node] + weight

            # If neighbor not visited or new path is shorter
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g  # Update shortest path
                parent[neighbor] = current_node  # Set parent for path reconstruction

                # f(n) = g(n) + h(n)
                f_cost = tentative_g + heuristic(neighbor, goal)

                # Push into priority queue
                heapq.heappush(open_set, (f_cost, neighbor))

    # If open_set empties without reaching goal → no path exists
    return None


def reconstruct_path(parent, goal):
    """
    Reconstructs the shortest path by traversing backward
    from the goal node using the parent dictionary.
    """
    path = []
    current = goal

    # Trace back from goal to start
    while current is not None:
        path.append(current)
        current = parent[current]

    # Reverse because we collected nodes backward
    return path[::-1]


# ---------------------- Example Usage ----------------------

# Sample graph represented as adjacency list
# Format: graph[node] = [(neighbor, weight), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 7)],
    'E': [('F', 1)],
    'F': []
}

# Simple heuristic: number of edges difference (dummy example)
def heuristic(node, goal):
    # In a real map, heuristic = straight-line distance
    estimate = {
        'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0
    }
    return estimate[node]

# Running A*
path = a_star(graph, 'A', 'F', heuristic)

print("Shortest path using A*:", path)
