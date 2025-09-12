# def second_largest_elem(x):
#     if len(x)<2:
#         return None
#
#     unique = list(set(x))
#     unique.sort()
#     result = unique[-2]
#     return result
#
#
#
# x = [10, 20, 4, 45, 99]
# print(second_largest_elem(x))

def kth_largest_elem(x,k):
    unique = list(set(x))
    unique.sort(reverse=True)
    if k<=len(unique):
        return unique[k-1]
    else:
        return None


x = [10, 20, 4, 45, 99]
print(kth_largest_elem(x,k=4))




