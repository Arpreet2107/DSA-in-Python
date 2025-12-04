# Additional: DFS-based Topological Sort (short)
# Mechanism

# Perform DFS and push nodes to a stack when exiting recursion (postorder). Reverse the stack to get topological order.

# Also :O(V+E).
def topo_dfs(adj):
    visited = set()                                    # visited set
    temp = set()                                       # temporary mark for cycle detection
    order = []                                         # list to push nodes in postorder

    def dfs(u):
        if u in temp:                                  # if temp mark seen again, cycle detected
            raise ValueError("Cycle detected")         # raise exception for cycle
        if u in visited:                               # if already permanently marked skip
            return
        temp.add(u)                                    # add to temporary mark
        for v in adj.get(u, []):                       # visit neighbors
            dfs(v)                                     # recursive DFS
        temp.remove(u)                                 # remove temporary mark on exit
        visited.add(u)                                 # permanently mark visited
        order.append(u)                                # append node after visiting neighbors

    for node in adj:                                   # run DFS from all nodes
        if node not in visited:
            dfs(node)
    order.reverse()                                    # reverse postorder to get topological order
    return order                                       # return topological ordering

