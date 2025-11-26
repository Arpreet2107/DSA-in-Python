def counting_sort(nums):
    # nums: list of non-negative integers to sort
    # returns: a new list containing the sorted elements (stable)

    if nums is None:                        # guard: if input is None
        return None                         # return None to indicate invalid input

    n = len(nums)                           # length of the input list
    if n <= 1:                              # if zero or one element, already sorted
        return nums[:]                      # return a shallow copy (non-destructive)

    max_val = max(nums)                     # find the maximum value in nums (range upper bound)
    # create count array of size max_val + 1 initialized to zeros
    count = [0] * (max_val + 1)             # count[i] will hold occurrences of value i

    # Step 1: Count occurrences
    for x in nums:                          # iterate through every element in input
        count[x] += 1                       # increment count for value x

    # Step 2: Accumulate counts so count[i] becomes number of elements <= i
    for i in range(1, len(count)):          # start from 1 because count[0] stays as-is
        count[i] += count[i - 1]            # accumulate previous counts into current

    # Step 3: Build output array of length n
    output = [0] * n                        # output will hold sorted elements

    # To keep stability, iterate input from right to left
    for x in reversed(nums):                # iterate reversed so equal items preserve original order
        pos = count[x] - 1                  # final position index in output for this x
        output[pos] = x                     # place x at its correct position
        count[x] -= 1                       # decrement count so next same value goes to previous index

    return output                           # return the sorted list (stable)
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]              # sample input (non-negative integers)
    print("Original:", arr)                  # show original
    sorted_arr = counting_sort(arr)          # sort using counting_sort
    print("Sorted:  ", sorted_arr)           # print sorted result
    print("Original unchanged:", arr)        # original remains unchanged
