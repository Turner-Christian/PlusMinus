# Given five positive integers,
# find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

arrays = [[1, 2, 3, 4, 5], [7, 69, 2, 221, 8974]]

def miniMaxSum(arr):
    return (sum(arr) - max(arr), sum(arr) - min(arr))

print('Example One:', miniMaxSum(arrays[0]), '\nExample Two:', miniMaxSum(arrays[1]))