# remove duplicate from sorted array

def remove_duplicate_from_sorted_array(x):
    if not x:
        return []

    result = [x[0]]

    for i in range(1,len(x)):
        if x[i] != x[i-1]:
            result.append(x[i])
    return result


x = [2,2,3,4,4,5,6,6]
print(remove_duplicate_from_sorted_array(x))
