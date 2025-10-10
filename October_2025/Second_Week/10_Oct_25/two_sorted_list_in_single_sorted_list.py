"""
two sorted list in singlte sorted list
"""
def two_sorted_list(l1,l2):
    l_new = l1 + l2
    return sorted(l_new)


l1 = [1,4,6]
l2 = [2,5,7]
print(two_sorted_list(l1,l2))
