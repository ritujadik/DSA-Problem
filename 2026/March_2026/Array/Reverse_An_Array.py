"""Reverse an Array"""

# first method
# def reverse_array(arr):
#     new_arr = arr[::-1]
#     return new_arr
#
#
#
# arr = [5,3,6,7,9,8]
# print(reverse_array(arr))

# second method

def reverse_new_arr(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[len(arr) - 1 - i])
    return new_arr

arr = [5,3,6,7,9,8]
print(reverse_new_arr(arr))