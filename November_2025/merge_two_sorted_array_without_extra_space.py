""" Merge two sorted array with extra space """

# def two_sorted_array(x1,x2):
#     n1 = len(x1)
#     n2 = len(x2)
#     i = j = 0
#     merged_list = []
#     while i< n1 and j<n2:
#         if x1[i] <= x2[j]:
#             merged_list.append(x1[i])
#             i+=1
#         else:
#             merged_list.append(x2[j])
#             j+=1
#
#     while i < n1:
#         merged_list.append(x1[i])
#         i+=1
#
#     while j<n2:
#         merged_list.append(x2[j])
#         j+=1
#     for i in range(n1):
#         x1[i] = merged_list[i]
#
#     for j in range(n2):
#         x2[j] = merged_list[n1+j]
#
#
#     return merged_list
#
#
# x1 = [1,3,5,7]
# x2 = [2,4,6,8]
# print(two_sorted_array(x1,x2))

""" Merge two sorted array with extra space """

def two_sorted_array(x1,x2):
    n1 = len(x1)
    n2 = len(x2)
    i = 0

    while i < n1:
        if x1[i] > x2[0]:
            x1[i], x2[0] = x2[0], x1[i]

            first = x2[0]
            k = 1
            while k < n2 and x2[k] < first:
                x2[k-1] = x2[k]
                k += 1

            x2[k-1] = first
        i += 1
    return x1,x2

x1 = [1,3,5,7]
x2 = [2,4,6,8]
print(two_sorted_array(x1,x2))











