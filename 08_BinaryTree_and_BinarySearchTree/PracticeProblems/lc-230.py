# ✅ LeetCode 230 — Kth Smallest Element in a BST
# 🌳 Key Idea

# In a Binary Search Tree (BST):

# Left subtree  <  Root  <  Right subtree


# An inorder traversal (Left → Node → Right) of a BST produces:

# A sorted list of all node values.


# So, the k-th smallest element is simply the k-th element in inorder order.

# 🔥 Approach 1 (Most Common): Inorder Traversal (DFS)
# Steps:

# Do inorder traversal.

# Keep counting values.

# When count == k → return value.
# Definition for a binary tree node.
# 💡 Why It Works

# Inorder traversal gives sorted order in BST.

# We only care about the k-th value.

# We stop early once we find the result → efficient.

# ⏱️ Time & Space Complexity
# | Type           | Value                                  |
# | -------------- | -------------------------------------- |
# | **Time**       | O(H + k) — best case, stops early      |
# | **Worst Case** | O(N)                                   |
# | **Space**      | O(H) recursion stack (H = tree height) |


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        # Inorder traversal list
        self.count = 0
        self.answer = None

        def inorder(node):
            if not node or self.answer is not None:
                return

            # Visit left subtree
            inorder(node.left)

            # Process current node
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return

            # Visit right subtree
            inorder(node.right)

        inorder(root)
        return self.answer
