# 🧩 Problem: LeetCode 54 — Spiral Matrix
# Problem Statement
# You are given an m x n matrix.
# You need to return all the elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self,matrix:list[list[int]])-> list[int]:
        res = []
        n = len(matrix)
        m = len(matrix[0])
        rowStart,rowEnd = 0,n-1
        colStart,colEnd = 0,m-1
        while rowStart <= rowEnd and colStart <= colEnd:
            #1. Traverse Left -> Right along the top row
            for col in range(colStart,colEnd+1):
                res.append(matrix[rowStart][col])
            rowStart += 1
            #2. Traverse Top -> Bottom along the rightmost column
            for row in range(rowStart,rowEnd+1):
                res.append(matrix[row][colEnd])
            colEnd -= 1
            #3. Traverse Right -> Left along the bottom row
            if rowStart <= rowEnd:
                for col in range(colEnd,colStart-1,-1):
                    res.append(matrix[rowEnd][col])
                rowEnd -= 1
            #4. Traverse Bottom -> Top along the leftmost column
            if colStart <= colEnd:
                for row in range(rowEnd,rowStart-1,-1):
                    res.append(matrix[row][colStart])
                colStart += 1
        return res
# Example usage:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
result = sol.spiralOrder(matrix)
print(result)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
