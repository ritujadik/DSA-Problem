
"""
Write a program to find the second largest element in the array.
"""

# def second_largest_elem(arr):
#     first_elem = second_elem = float('-inf')
#     for elem in arr:
#         if elem > first_elem:
#             second_elem = first_elem
#             first_elem = elem
#     return second_elem if second_elem != float('-inf') else None
#
# arr = [3,4]
# print(second_largest_elem(arr))

"""
Write a program to rotate a list by k position
"""
# def rotate(arr,k):
#     n = len(arr)
#     new_arr = []
#     for i in range(n):
#         new_arr = arr[:k][::-1] + arr[k:]
#     return new_arr
#
#
#
# arr = [1,2,4,5,3,7,8]
# k =4
#

"""
Write a program in a list to find all the pairs in a list whose sum is equal to the given number
"""
# def all_pair(arr,k):
#     # it is the first approach for solve this question
#     # new_arr = []
#     # for i in range(0,len(arr)):
#     #     for j in range(i+1,len(arr)):
#     #             sum = arr[i] + arr[j]
#     #             if sum == k:
#     #                 new_arr.append((arr[i],arr[j]))
#     # return new_arr
#     seen = set()
#     new_arr = []
#     for i in range(len(arr)):
#         target = k-arr[i]
#         if target in seen:
#             new_arr.append((target,arr[i]))
#         seen.add(arr[i])
#     return new_arr
#
#
#
#
# arr = [2,3,5,7,1,8,4]
# k = 8
# print(all_pair(arr,k))


"""
Write a program to split a list into chunks of size n
"""
# def split_into_chunks(arr, n):
#     for i in range(0, len(arr), n):
#         yield arr[i:i + n]
#
#
# arr = [1,2,3,4,5,6,7,8,9,10]
# n = 3
# print(list(split_into_chunks(arr, n)))


"""
Write a program to replace all occurence of an element in a list with another value
"""
# def replace_occurence(arr,old_value,new_value):
#     for i in range(len(arr)):
#         if arr[i] == old_value:
#             arr[i] = new_value
#     return arr
#
# arr = [1,2,3,4,5,2,7,2,9,10]
# old_value = 2
# new_value = 11
# print(replace_occurence(arr,old_value,new_value))


""" 
Write a program to find the index of all occurence of the specific element
"""
# def find_index(arr,value):
#     new_arr = []
#     for i in range(len(arr)):
#         if arr[i] == value:
#             new_arr.append(i)
#     return new_arr
#
# arr = [1,2,3,4,5,2,7,2,9,10]
# value = 2
# print(find_index(arr,value))


"""
Write a program to check if the two lists are permutation of each other
"""
# def check_permutation(lst1,lst2):
#     if len(lst1) != len(lst2):
#         return False
#     lst1.sort()
#     lst2.sort()
#     return lst1 == lst2
#
#
#
# lst1 = [2,3,4]
# lst2 = [5,6,7]
# print(check_permutation(lst1,lst2))

"""Write a program to interleave two lists of the same length"""
# def interleave(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     result = []
#     for i in range(len(list1)):
#         result.append(list1[i])
#         result.append(list2[i])
#     return result
#
#
# list1 = [1,4,5]
# list2 = [4,5,6]
# print(interleave(list1, list2))


"""
Write a program to find the missing numbers from a list of integers in a given range
"""
def find_missing_numbers(arr,start,end):
    result = []
    for i in range(start,end + 1):
        if i not in arr:
            result.append(i)
    return result

arr = [1,2,6]
start = 1
end = 6
print(find_missing_numbers(arr,start,end))