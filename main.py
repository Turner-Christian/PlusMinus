# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal

arrays = [[-4, 3, -9, 0, 4, 1], [1, 2, 3, -1, -2, -3, 0, 0]]

def plusMinus(arr):
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    
    positiveDecimal = ("{:.6f}".format(positive / len(arr)))
    negativeDecimal = ("{:.6f}".format(negative / len(arr)))
    zeroDecimal = ("{:.6f}".format(zero / len(arr)))
    print("Positive : " , positiveDecimal , "\nNegative: " , negativeDecimal, "\nZero: " , zeroDecimal)
    return 'Complete'

print(plusMinus(arrays[0]), plusMinus(arrays[1]))