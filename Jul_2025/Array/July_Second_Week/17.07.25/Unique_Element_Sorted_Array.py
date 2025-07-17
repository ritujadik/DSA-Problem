# Unique Element in sorted array

#First Approach
# def unique_element_in_sorted_array(x):
#     new_x = set(x)
#
#     return len(new_x)
#
#
#
# x = [1,2,3,3,3,4,5,5]
# print(unique_element_in_sorted_array(x))

# def remove_duplicate_from_sorted_array(x):
#     left = 0
#     right = len(x)-1
#     while left<right:
#         if x[left] == x[left+1]:
#             x.pop(left)
#             right-=1
#         else:left+=1
#     return len(x)
#
# x = [1,3,3,3,4,4]
# remove_duplicate_from_sorted_array(x)
# print(remove_duplicate_from_sorted_array(x))

def remove_duplicate_from_sorted_array(x):
    if not x:
        return 0
    write = 1
    for read in range(1, len(x)):
        if x[read] != x[read - 1]:
            x[write] = x[read]
            write += 1
    return write


x = [1,1,1,1,2,2]
print(remove_duplicate_from_sorted_array(x))