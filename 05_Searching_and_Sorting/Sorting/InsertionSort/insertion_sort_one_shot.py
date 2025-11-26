from typing import List  # Import List for type hints (helps readability and tools)

def insertion_sort(arr: List[int]) -> None:
    # This function sorts the list 'arr' in-place in ascending order using insertion sort.
    # It returns None because the sorting modifies the original list.

    n = len(arr)  # Get the number of elements in the list and store in variable n

    # Start from index 1 because a single-element list at index 0 is already "sorted"
    for i in range(1, n):  # i is the index of the element we want to insert into the sorted left side
        key = arr[i]  # Save the value at index i (the "card" to insert) into variable key
        j = i - 1  # j will be used to scan the sorted portion to the left of i, starting from i-1

        # Shift elements in arr[0..i-1] that are greater than key to one position to the right
        # This loop continues while j is within bounds and the element at j is greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move the element at arr[j] one position to the right
            j -= 1  # Move the index j one position left to continue checking

        # After shifting larger elements, place the key into its correct sorted position
        arr[j + 1] = key  # Insert key at the position after the last shifted element


# ---------------- MAIN FUNCTION FOR DEMO ----------------
def main():
    # Prompt the user to enter integers separated by spaces
    raw = input("Enter integers separated by space: ")  # Read raw input string from the user

    # Convert the raw input string into a list of integers
    nums = list(map(int, raw.strip().split())) if raw.strip() != "" else []  # Handle empty input safely

    # Print the array before sorting so we can compare
    print("Before sorting:", nums)  # Show initial array state

    # Call insertion_sort to sort the list in-place
    insertion_sort(nums)  # Sorts nums directly; no return value expected

    # Print the array after sorting to verify result
    print("After sorting: ", nums)  # Show final sorted array


# Ensure main runs only when the script is executed directly (not when imported)
if __name__ == "__main__":
    main()  # Execute the demo main function
