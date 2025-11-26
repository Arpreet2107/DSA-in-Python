# Bubble Sort implementation inside a LeetCode-style Solution class
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Get the number of elements in the list
        n = len(nums)

        # Outer loop → runs n times (or until no swap happens)
        for i in range(n):

            # Boolean flag to check if any swap occurred in this pass
            isSwap = False

            # Inner loop → compares each adjacent pair
            # We run only till n-i-1 because after every pass,
            # the largest element moves to the end and does not need checking again
            for j in range(n - i - 1):

                # If the current element is greater than the next one,
                # they are in the wrong order → swap them
                if nums[j] > nums[j + 1]:
                    temp = nums[j]              # Store current element
                    nums[j] = nums[j + 1]        # Replace current with next
                    nums[j + 1] = temp           # Place stored value in next position

                    isSwap = True  # Mark that a swap happened in this pass

            # If no swap took place in the entire pass,
            # the array is already sorted → break early
            if not isSwap:
                break

        # Return the sorted array
        return nums


# ---------------------- MAIN FUNCTION ----------------------
# This main function will allow you to run the sorting code manually
# (LeetCode will ignore this part, but it is useful for local testing)
def main():
    # Take user input: space-separated integers
    input_nums = list(map(int, input("Enter numbers separated by space: ").split()))

    # Create an object of Solution class
    obj = Solution()

    # Call the sortArray function
    sorted_nums = obj.sortArray(input_nums)

    # Print the sorted output
    print("Sorted Array:", sorted_nums)


# Ensures the main() function runs only when the file is executed directly
if __name__ == "__main__":
    main()
