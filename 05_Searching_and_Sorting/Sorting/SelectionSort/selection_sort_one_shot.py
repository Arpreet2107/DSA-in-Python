from typing import List  # type hinting for better readability and tools

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Selection Sort (in-place).
        Args:
            nums: List[int] -- the list to be sorted (modified in place)
        Returns:
            The same list `nums`, sorted in ascending order.
        """
        n = len(nums)                     # store length of the list in variable n

        # Outer loop: move the boundary of the sorted part one step to the right each time
        for i in range(n - 1):            # we do n-1 passes; last element will already be in place
            min_index = i                # assume the minimum is at the current index i

            # Inner loop: find the index of the minimum element in nums[i+1 .. n-1]
            for j in range(i + 1, n):    # check each position j after i
                # If we find a smaller element than current minimum, update min_index
                if nums[j] < nums[min_index]:
                    min_index = j       # new minimum's index

            # After the inner loop, min_index holds the index of the smallest element in the unsorted part

            # Swap the found minimum element with the element at index i to expand the sorted part
            # Swapping even when min_index == i is okay (it's a no-op swap)
            nums[i], nums[min_index] = nums[min_index], nums[i]

        # After all passes, nums is sorted; return it (LeetCode-style expects a return)
        return nums


# ------------------ MAIN FUNCTION (for local testing) ------------------
def main():
    # Prompt the user to enter integers separated by spaces.
    # Example input: 64 25 12 22 11
    raw_input_str = input("Enter integers separated by spaces: ").strip()

    # Convert the input string into a list of integers.
    # If the user enters an empty string, produce an empty list.
    nums = list(map(int, raw_input_str.split())) if raw_input_str != "" else []

    # Print the array before sorting for clarity
    print("Before sorting:", nums)

    # Create Solution object and call sortArray to sort the list
    solution = Solution()
    sorted_nums = solution.sortArray(nums)  # sortArray sorts in-place but also returns the list

    # Print the sorted list
    print("After  sorting:", sorted_nums)


# This ensures main() runs only when the script is executed directly,
# and not when the file is imported as a module in another script.
if __name__ == "__main__":
    main()
