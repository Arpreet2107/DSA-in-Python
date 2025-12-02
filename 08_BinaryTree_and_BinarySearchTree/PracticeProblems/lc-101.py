# ✅ LeetCode 101 — Symmetric Tree

# A binary tree is symmetric if:

# The left subtree is a mirror of the right subtree.


# This means:

# Left subtree’s left child == Right subtree’s right child

# Left subtree’s right child == Right subtree’s left child

# This is checked recursively.

# 🌟 Intuition

# Think of symmetry like a mirror image:

#       1
#     /   \
#    2     2
#   / \   / \
#  3  4  4  3    → Symmetric


# But:

#       1
#     /   \
#    2     2
#     \      \
#      3      3    → NOT symmetric

# ✅ Approach: Recursion

# We define a helper function:

# isMirror(left, right)


# It checks if two trees are mirror images.

# Rules:

# If both nodes are None → symmetric

# If only one is None → not symmetric

# If values differ → not symmetric

# Recursively check mirror children

# left.left with right.right

# left.right with right.left
# Definition for a binary tree node.
# 🧩 Time & Space Complexity
# | Complexity | Value                                               |
# | ---------- | --------------------------------------------------- |
# | Time       | **O(N)** — every node visited once                  |
# | Space      | **O(H)** — recursion stack (worst case skewed tree) |

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        # A tree is symmetric if left and right subtrees are mirror images
        def isMirror(left, right):
            # Case 1: both are None -> symmetric
            if not left and not right:
                return True
            
            # Case 2: one is None -> not symmetric
            if not left or not right:
                return False
            
            # Case 3: values differ -> not symmetric
            if left.val != right.val:
                return False
            
            # Case 4: check mirror children
            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)
