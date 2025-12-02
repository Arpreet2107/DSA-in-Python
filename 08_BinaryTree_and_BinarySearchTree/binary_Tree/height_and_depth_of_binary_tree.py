def height(root):
    # Height of empty tree = 0
    if root is None:
        return 0
    # height = 1 + max(height(left), height(right))
    return 1 + max(height(root.left), height(root.right))
