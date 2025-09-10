def merge_two_sorted_array(l1,l2):
    n1 = len(l1)
    n2 = len(l2)
    i = j = 0
    new_sorted_array = []

    while i<n1 and j <n2:
        if l1[i] <= l2[j]:
            new_sorted_array.append(l1[i])
            i+=1
        else:
            new_sorted_array.append(l2[j])
            j+=1

    while i<n1:
        new_sorted_array.append(l1[i])
        i+=1

    while j<n2:
        new_sorted_array.append(l2[j])
        j+=1

    return new_sorted_array

l1 = [1,2,3,4,5,6]
l2 = [2,3,4,7,8]

print(merge_two_sorted_array(l1,l2))