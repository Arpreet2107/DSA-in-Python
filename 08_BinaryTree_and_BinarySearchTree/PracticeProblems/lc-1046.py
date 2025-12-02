# ✅ LeetCode 1046 — Last Stone Weight (Python Solution with Comments)
# 🧠 Problem Summary

# You are given an array of stones. Every turn, you smash the two heaviest stones:

# If they are equal, both get destroyed.

# If they are unequal, the larger one becomes larger - smaller.

# Continue until 0 or 1 stones remain.

# Return the weight of the last remaining stone (or 0).
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        """
        Use a max-heap (simulated with negative values because Python has min-heap)
        Always remove the two heaviest stones and smash them.
        """
        
        # Convert stones list into a max-heap by negating every value
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)  # heapify the list

        # Keep smashing until 0 or 1 stones left
        while len(max_heap) > 1:
            # Pop two largest stones (smallest negatives)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            # If they are not equal, push the difference back
            if stone1 != stone2:
                new_stone = stone1 - stone2
                heapq.heappush(max_heap, -new_stone)

        # Return the last stone or 0
        return -max_heap[0] if max_heap else 0


# ---------------------- MAIN FUNCTION ----------------------
def main():
    # Example input
    stones = [2, 7, 4, 1, 8, 1]

    solution = Solution()
    result = solution.lastStoneWeight(stones)

    print("Last stone weight:", result)


# Run main only if this file is executed directly
if __name__ == "__main__":
    main()
