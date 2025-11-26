def merge(left, right):
    # 'left'  -> a sorted list (left half)
    # 'right' -> a sorted list (right half)
    # We'll merge them into a single sorted list and return it.

    merged = []                 # Create an empty list to hold merged result
    i = 0                       # Pointer for left list, starts at its first element
    j = 0                       # Pointer for right list, starts at its first element

    # Continue while there are elements in both lists to compare
    while i < len(left) and j < len(right):
        # Compare current elements from both lists
        if left[i] <= right[j]:
            # If left element is smaller or equal, append it to merged
            # Using <= keeps stability: left element comes before equal right.
            merged.append(left[i])
            i += 1              # Move pointer in left list forward
        else:
            # Right element is smaller, append it
            merged.append(right[j])
            j += 1              # Move pointer in right list forward

    # After the loop, at least one list is exhausted.
    # Append any remaining elements from left (if any).
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Append any remaining elements from right (if any).
    while j < len(right):
        merged.append(right[j])
        j += 1

    # 'merged' now contains all elements from left and right, in sorted order.
    return merged


def merge_sort(arr):
    # Input: arr -> list of comparable items (e.g., numbers)
    # Output: new sorted list (does not modify the input list in-place)

    # Base case: a list of length 0 or 1 is already sorted, return it.
    if len(arr) <= 1:
        return arr[:]           # return a shallow copy to be explicit

    # Recursive case: split the list into two halves and sort each half.
    mid = len(arr) // 2        # Find middle index; // is integer division
    left_half = arr[:mid]      # Left half: from start up to (but not including) mid
    right_half = arr[mid:]     # Right half: from mid to end

    # Recursively sort the left half. This call will further split until base case.
    sorted_left = merge_sort(left_half)

    # Recursively sort the right half.
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves and return the merged sorted list.
    return merge(sorted_left, sorted_right)


# Example usage and a small test to demonstrate behavior
if __name__ == "__main__":
    # Example unsorted list
    example = [38, 27, 43, 3, 9, 82, 10]

    # Print original list
    print("Original:", example)

    # Sort using merge_sort. This returns a new sorted list.
    sorted_example = merge_sort(example)

    # Print sorted result
    print("Sorted:  ", sorted_example)

    # Confirm original list was not modified by merge_sort (demonstrates non-in-place behavior)
    print("Original after sort (unchanged):", example)
