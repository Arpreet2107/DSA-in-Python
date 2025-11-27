# 🔢 LeetCode 74 — Search a 2D Matrix
# Problem Summary

# You are given a 2D matrix where:

# Each row is sorted in ascending order

# The first element of each row is greater than the last element of the previous row

# Example:

# [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 60]
# ]


# This matrix behaves like a single sorted 1D array.

# Your task: Search for a target value using O(log(m*n)) time.

# 🔥 Key Insight

# Flatten the matrix conceptually:

# 1,3,5,7,10,11,16,20,23,30,34,60


# We don’t actually flatten it.
# Instead, we map 1D index → 2D coordinates.

# 🧠 Index Mapping Formula

# For a matrix with:

# rows = m

# cols = n

# For a given mid in the range [0, m*n - 1]:

# row = mid // n
# col = mid % n


# This gives exact location of the element.

# 🔍 Binary Search Strategy

# Search between:

# left = 0
# right = m*n - 1


# Mid element = matrix[mid // n][mid % n]

# Compare with target like normal binary search.
class Solution:
    def searchMatrix(self, matrix, target):
        # Number of rows and columns
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1

        # Binary search on the imaginary 1D array
        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n

            value = matrix[row][col]  # actual matrix element

            # Case 1: target found
            if value == target:
                return True

            # Case 2: target is smaller → move left
            elif value > target:
                right = mid - 1

            # Case 3: target is larger → move right
            else:
                left = mid + 1

        # Target not found
        return False
