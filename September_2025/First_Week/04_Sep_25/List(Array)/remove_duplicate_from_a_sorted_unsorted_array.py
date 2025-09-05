def remove_duplicate_elem(x):
    left = 0
    right = len(x)-1
    unique = []

    while left<right:
        if x[left] not in unique:
            unique.append(x[left])
        if x[right] not in unique:
            unique.append(x[right])
        left+=1
        right-=1

    return unique


x = [2,3,4,3,5,2,4]
print(remove_duplicate_elem(x))