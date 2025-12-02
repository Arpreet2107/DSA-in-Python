# binary_tree.py

class Node:
    """Node of a binary tree with 'val', 'left', and 'right' references."""
    def __init__(self, val):
        self.val = val      # store value
        self.left = None    # left child
        self.right = None   # right child

# Example: build a small binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
if __name__ == "__main__":
    root = Node(1)         # create root node with value 1
    root.left = Node(2)    # left child 2
    root.right = Node(3)   # right child 3
    root.left.left = Node(4)   # 2's left child 4
    root.left.right = Node(5)  # 2's right child 5

    # Now root is the tree shown above
