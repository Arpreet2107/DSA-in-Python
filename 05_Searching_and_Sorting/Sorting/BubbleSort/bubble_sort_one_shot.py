def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Sorts a list in ascending order by repeatedly swapping
    adjacent elements that are in the wrong order.
    """

    n = len(arr)  # Number of elements in the list

    # Outer loop → runs (n - 1) times
    for i in range(n - 1):

        # This flag checks if any swap happened in this pass
        # If no swap occurs, array is already sorted → stop early
        swapped = False

        # Inner loop → compares adjacent elements
        # Each pass pushes the largest remaining element to the end
        for j in range(n - 1 - i):

            # If the current element is greater than the next one
            # then they are in the wrong order → swap them
            if arr[j] > arr[j + 1]:

                # Swapping the two adjacent values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Mark that a swap has happened
                swapped = True

        # If no swap happened during the entire pass,
        # it means the list is already sorted → exit early
        if not swapped:
            break


# ---------------- MAIN FUNCTION ----------------
def main():
    # Take array input from user
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Original array:", arr)

    # Call the bubble_sort function
    bubble_sort(arr)

    print("Sorted array:", arr)


# Run main only when executed directly
if __name__ == "__main__":
    main()
