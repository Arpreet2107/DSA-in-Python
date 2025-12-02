def preorder(root):
    # Visit root, then left subtree, then right subtree
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
def inorder(root):
    # For BST, inorder returns sorted order
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
def postorder(root):
    # Use for deleting tree or computing subtree values
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
from collections import deque

def level_order(root):
    # BFS using a queue; returns list of values by level
    if root is None:
        return []
    q = deque([root])              # queue of nodes to visit
    res = []
    while q:
        node = q.popleft()         # dequeue
        res.append(node.val)
        if node.left:
            q.append(node.left)    # enqueue left
        if node.right:
            q.append(node.right)   # enqueue right
    return res
