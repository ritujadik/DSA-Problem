"""
Given an array of integers arr[] of size n,the task is to rotate the array elements to the left by d positions
"""

# def rotate_arr(arr,d):
#     new_arr = []
#     n  = len(arr)
#     d = d%n
#     for i in range(n):
#         new_arr.append(arr[(i+d)%n])
#
#     return new_arr
#
#
# arr = [1,2,3,4,5,6]
# print(rotate_arr(arr,2))

# Second way to do the same
def rotate_arr(arr,d):
    d = d%len(arr)
    return arr[d:] + arr[:d]

arr = [1,2,3,4,5,6]
print(rotate_arr(arr,2))
