# Linear Search Algorithm
def linear_search(arr, target):
    # Loop over every index from 0 to len(arr)-1
    for i in range(len(arr)):
        
        # Check if current element matches the target
        if arr[i] == target:
            return i  # Found! Return its index
        
    # If loop finishes, element does not exist in list
    return -1


# Example usage:
arr = [10, 30, 50, 20, 60, 80]
target = 20

result = linear_search(arr, target)
print("Element found at index:", result)

# Binary Search Algorithm (requires sorted array)
def binary_search(arr, target):
    # We maintain two pointers: left and right
    left = 0
    right = len(arr) - 1
    
    # Continue searching while left does not cross right
    while left <= right:
        
        # Find mid index (floor division)
        mid = (left + right) // 2
        
        # Case 1: Target found
        if arr[mid] == target:
            return mid
        
        # Case 2: Target is smaller → search in left half
        elif arr[mid] > target:
            right = mid - 1
        
        # Case 3: Target is larger → search in right half
        else:
            left = mid + 1
    
    # If we exit loop, target is not in array
    return -1


# Example usage:
arr = [10, 20, 30, 40, 50, 60]
target = 50

result = binary_search(arr, target)
print("Element found at index:", result)

# Recursive Binary Search Algorithm
def binary_search_recursive(arr, left, right, target):

    # Base case: element not found
    if left > right:
        return -1

    # Find the mid index
    mid = (left + right) // 2

    # Case 1: Found target
    if arr[mid] == target:
        return mid
    
    # Case 2: Search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, left, mid-1, target)
    
    # Case 3: Search right half
    else:
        return binary_search_recursive(arr, mid+1, right, target)


# Example usage:
arr = [5, 12, 18, 25, 36, 49]
target = 25

result = binary_search_recursive(arr, 0, len(arr)-1, target)
print("Element found at index:", result)
