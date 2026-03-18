""""Second Largest Element"""

# def second_largest_element(arr):
#    new_arr = set(arr)
#    new_arr = sorted(new_arr)
#    return new_arr[-2]
#
#
#
#
# arr = [3,6,1,8,9,9,2,7]
# print(second_largest_element(arr))


def second_largest_element(arr):
    largest = second_largest = float('-inf')
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    return second_largest

arr = [3,6,1,8,9,9,2,7]
print(second_largest_element(arr))