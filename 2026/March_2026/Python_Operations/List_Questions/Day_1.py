"""" Write a Python program to reverse a list without using the reverse() method"""

# def reverse(arr):
#     n = len(arr)
#     new_arr = []
#     for i in range(n):
#         j = (n-1-i)
#         new_arr.append(arr[j])
#     return new_arr
#
#
#
# arr = [3,1,2,8,5,8,9]
# print(reverse(arr))

"""
Write a Python Program to find the largest and smallest elements in a list
"""
# def largest_smallest(arr):
#     n = len(arr)
#     max_elem = arr[0]
#     min_elem = arr[0]
#     for i in range(1,n):
#         if arr[i] > max_elem:
#             max_elem = arr[i]
#         elif arr[i] < min_elem:
#             min_elem = arr[i]
#     return max_elem, min_elem
#
# arr = [3,1,2,8,5,8,9]
# print(largest_smallest(arr))

"""
Write a Python program to remove all the duplicates from a list
"""
# def remove_duplicates(arr):
#     n = len(arr)
#     new_arr = []
#     i = 0
#     while i < n:
#         if arr[i] not in new_arr:
#             new_arr.append(arr[i])
#         i+=1
#     return new_arr
#
#
# arr = [2, 3, 1, 8, 5, 6, 3, 5, 3, 1]
# print(remove_duplicates(arr))

"""
Write a program to merge two lists and remove duplicates
"""

# def mege_and_remove(arr1, arr2):
#     i = j = 0
#     new_arr = []
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             if not new_arr or new_arr[-1] != arr1[i]:
#                 new_arr.append(arr1[i])
#             i += 1
#         elif arr1[i] >arr2[i]:
#             if not new_arr or new_arr[-1] != arr2[j]:
#                 new_arr.append(arr2[j])
#             j += 1
#         else:
#             if not new_arr or new_arr[-1] != arr1[i]:
#                 new_arr.append(arr1[i])
#
#             i+=1
#             j+=1
#     while i < len(arr1):
#         if not new_arr or new_arr[-1] != arr1[i]:
#             new_arr.append(arr1[i])
#         i+=1
#     while j < len(arr2):
#         if not new_arr or new_arr[-1] != arr2[j]:
#             new_arr.append(arr2[j])
#         j+=1
#     return new_arr
#
#
# arr1 = [2, 3, 1, 8, 5, 6, 5]
# arr2 = [5,2,7,8,9,4]
# print(mege_and_remove(arr1, arr2))


"""
Write a Python program to find the common elements between two lists
"""

# def common_elem(list1, list2):
#     n1 = len(list1)
#     new_list = []
#     for i in list1:
#         if i in list2 and i not in new_list:
#                 new_list.append(i)
#     return new_list
#
#
# arr1 = [2, 3, 1, 8, 5, 6]
# arr2 = [5,2,7,8,9,4]
# print(common_elem(arr1, arr2))

""" Write a Program to flatten a nested list"""
# def flatten(lst1):
#     flat_list = []
#     for i in lst1:
#         for j in i:
#             flat_list.append(j)
#
#     return flat_list
#
# lst1 = [[1,2],[3,4],[5,6],[7,8]]
# print(flatten(lst1))

""" Write a Program to check if a list is a palindrome"""

# def check_palindrome(lst):
#
#     new_lst = lst[::-1]
#     if lst == new_lst:
#         return True
#     else:
#         return False
#
# lst1 = [1,2,2,1]
# print(check_palindrome(lst1))


# """ Write a program to count the frequency of each element in a list"""
# def freq_count(arr):
#     freq = {}
#     for i in arr:
#         if i in freq.keys():
#             freq[i] += 1
#         else:
#             freq[i] = 1
#
#     return freq
#
# arr  = [1,2,3,1,3,9,7,4,5,2,7,2,9,8]
# print(freq_count(arr))



"""
Write a program to sort a list of dictionaries by a key
"""

# def dict_list(arr,key):
#     new_arr = sorted(arr,key = lambda x:x[key])
#     return new_arr
#
# arr =  [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Charlie", "age": 30}
# ]
# key = "age"
# print(dict_list(arr,key))


"""
Write a program to move all zeros in a list to the end without changing the order of the other elements
"""
def move_zeros(arr):
    i = 0
    n = len(arr)
    for j in range(n):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
    while i < n:
        arr[i] = 0
        i += 1
    return arr

arr = [1,0,2,3,0,4,0,5,0,7]
print(move_zeros(arr))