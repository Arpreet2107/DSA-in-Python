class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_search(root, key):
    # Iterative search for key in BST
    cur = root
    while cur:
        if key == cur.val:
            return cur
        elif key < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return None  # not found

def bst_insert(root, key):
    # Insert and return root (handles empty tree)
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)
    return root


def find_min(node):
    while node.left:
        node = node.left
    return node

def bst_delete(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = bst_delete(root.left, key)
    elif key > root.val:
        root.right = bst_delete(root.right, key)
    else:
        # found node to delete
        if root.left is None:
            return root.right     # case 1 or 2
        elif root.right is None:
            return root.left
        # case 3: two children -> find inorder successor
        succ = find_min(root.right)
        root.val = succ.val
        root.right = bst_delete(root.right, succ.val)
    return root


def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        # node value must be strictly between low and high
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    import math
    return helper(root, -math.inf, math.inf)


# avl.py

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1   # node height

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(y):
    # Right rotation:
    #     y               x
    #    / \    ->      /   \
    #   x   T3         T1    y
    #  / \                   / \
    # T1  T2                T2  T3
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    # update heights
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    # Left rotation:
    #   x                y
    #  / \     ->      /   \
    # T1  y           x    T3
    #    / \         / \
    #   T2 T3       T1 T2
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def avl_insert(node, key):
    # Standard BST insert
    if not node:
        return AVLNode(key)
    if key < node.val:
        node.left = avl_insert(node.left, key)
    else:
        node.right = avl_insert(node.right, key)
    # Update height
    update_height(node)
    # Check balance
    balance = get_balance(node)
    # Left Left
    if balance > 1 and key < node.left.val:
        return rotate_right(node)
    # Right Right
    if balance < -1 and key > node.right.val:
        return rotate_left(node)
    # Left Right
    if balance > 1 and key > node.left.val:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    # Right Left
    if balance < -1 and key < node.right.val:
        node.right = rotate_right(node.right)
        return rotate_left(node)
    return node
