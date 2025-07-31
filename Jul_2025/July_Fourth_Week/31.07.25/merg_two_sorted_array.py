"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

def two_sorted_list(x1,x2):
    i,j= 0,0
    n1 = len(x1)
    n2 = len(x2)
    result = []
    while i < n1 and j < n2:
        if x1[i] < x2[j]:
            result.append(x1[i])
            i+=1
        else:
            result.append(x2[j])
            j+=1

    while i < n1:
        result.append(x1[i])
        i+=1
    while j<n2:
        result.append(x2[j])
        j+=1

    return result


x1 = [1,2,4]
x2 = [1,3,4]
print(two_sorted_list(x1,x2))
