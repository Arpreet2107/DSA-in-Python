class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers
        left = 0
        right = len(numbers) - 1 

        # Loop until pointers meet
        while left < right:
            # Calculate current sum
            sum1 = numbers[left] + numbers[right]

            # If perfect match found → return 1-based indices
            if sum1 == target:
                return [left + 1, right + 1]

            # If sum is too large → decrease right pointer to reduce sum
            elif sum1 > target:
                right -= 1

            # If sum is too small → increase left pointer to increase sum
            else:
                left += 1

 
# -------------------- MAIN FUNCTION --------------------
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]   # Sorted input list
    target = 9                 # Desired sum

    obj = Solution()           # Create object of Solution class
    result = obj.twoSum(numbers, target)

    print("Indices:", result)  # Expected Output → [1, 2]
