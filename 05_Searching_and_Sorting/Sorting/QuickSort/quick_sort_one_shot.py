import random                            # import random so we can pick a random pivot

def lomuto_partition(arr, low, high):
    # Lomuto partition: partitions arr[low..high] around a pivot chosen at arr[high]
    # Returns the index of the pivot after partitioning (final pivot position).
    pivot = arr[high]                     # choose pivot as the last element in the segment
    i = low - 1                           # i will track the boundary of elements <= pivot
    j = low                               # j iterates through the segment to compare with pivot

    # Iterate over each element in arr[low..high-1]
    while j <= high - 1:
        # If current element is <= pivot, expand the <=-pivot region
        if arr[j] <= pivot:
            i += 1                        # move the boundary forward
            arr[i], arr[j] = arr[j], arr[i]  # swap current element into the <=-pivot region
        j += 1                            # move to next element to compare

    # After loop, place pivot right after the last <=-pivot element
    arr[i+1], arr[high] = arr[high], arr[i+1]  # swap pivot into its final sorted position
    return i + 1                          # return pivot's final index

def quicksort_inplace(arr, low, high):
    # Sort the subarray arr[low..high] in-place using Quick Sort
    if low < high:                        # only sort if the segment has 2 or more elements
        # Randomized pivot: pick a random index between low and high
        pivot_index = random.randint(low, high)  # randomly choose a pivot index
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # move chosen pivot to end

        # Partition around the pivot (which is now at arr[high])
        p = lomuto_partition(arr, low, high)  # p is the final index of the pivot

        # Recursively sort the left subarray (elements <= pivot) left of pivot
        quicksort_inplace(arr, low, p - 1)

        # Recursively sort the right subarray (elements > pivot) right of pivot
        quicksort_inplace(arr, p + 1, high)

def quick_sort(arr):
    # Public helper that sorts the entire list in-place and returns it for convenience
    # We copy the list if we want a non-destructive sort; here we sort in-place.
    if arr is None:                        # guard against None input
        return None
    n = len(arr)                           # length of the array
    if n <= 1:                             # if array has 0 or 1 element it's already sorted
        return arr                         # return as-is (no work needed)
    quicksort_inplace(arr, 0, n - 1)       # call the recursive in-place quicksort
    return arr                             # return the sorted array (same object, now sorted)

# Example usage and simple test
if __name__ == "__main__":
    example = [38, 27, 43, 3, 9, 82, 10]  # sample unsorted array
    print("Original:", example)           # show original
    sorted_example = quick_sort(example)  # sort in-place; returned value is same list now sorted
    print("Sorted:  ", sorted_example)    # print the sorted array
