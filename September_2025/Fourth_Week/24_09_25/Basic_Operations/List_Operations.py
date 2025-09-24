"""
What happens when you perform list1 + list 2 in python
"""

# def sum(l1,l2):
#
#     return l1 + l2
#
#
# l1 = [1,2]
# l2 = [4,3]
#
# # print(sum(l1,l2))
""" Reverse a list"""
def reverse_a_list(x):
    return x[::-1]

x =[1, 2, 3, 4]
print(reverse_a_list(x))

def sum_of_all_elememts(x):
    return sum(x)

x = [1,2,3,4]
print(sum_of_all_elememts(x))


""" find the duplicate in list"""

def duplicate(x):
    x_new = []
    i = 0
    while i <len(x):
        if x[i] in x[i+1:]:
            if x[i] not in x_new:
                x_new.append(x[i])
        i+=1
    return x_new

x = [1, 2, 3, 1, 2, 4]
print(duplicate(x))

"""
Write a function to check if one list is a sublist of another
"""
def is_sublist(l1,l2):
    return any(l1 == l2[i:i+len(l1)] for i in range(len(l2)-len(l1) + 1))
print(is_sublist([2, 3], [1, 2, 3, 4]))

"""
write a function to remove all occurence of a specific value from a list
"""
def occurence(x,val):
    return [i for i in x if i != val]
x = [1,2,4,3,2]
val = 2
print(occurence(x,val))

"""
write a function to find the index of specific value else return -1
"""
def elem_index(x,val):
    try:
        return (x.index(val))
    except ValueError:
        return -1


print(elem_index([1,2,3,4],2))

"""
write a function to merge the two list and remove duplicates
"""
def merge_two_list(l1,l2):
    return set(l1+l2)

"""
write a function to sort list in 
"""
def sort_list(x):
    return sorted(x,reverse=True)

x = [1,3,4,2,9,8]
print(sort_list(x))

def sort_list(x):
    return sorted(x,reverse=False)

x = [1,3,4,2,9,8]
print(sort_list(x))

"""
find the common elements between two lists
"""
def common_elem(l1,l2):
    return list(set(l1) & set(l2))

l1 = [2,3,4,7]
l2 = [1,2,5,3,4]
print(common_elem(l1,l2))