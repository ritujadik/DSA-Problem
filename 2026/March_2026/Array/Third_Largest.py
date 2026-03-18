""""Third largest number"""

def third_largest(arr):
    largest = second_largest = third_largest = float("-inf")
    for i in arr:
        if i>largest:
            third_largest = second_largest
            second_largest = largest
            largest = i
        elif i>second_largest and i != largest:
            third_largest = second_largest

        elif i>third_largest and i != second_largest and i != largest:
            third_largest = i

    return third_largest

arr = [3,6,1,8,9,9,2,7]
print(third_largest(arr))