def remove_duplicates(arr):
    seen = {}
    for i in arr:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]= 1
    result = []
    for key in seen:
        if seen[key] == 1:
            result.append(key)
    return result



arr = [1,2,4,3,2,1,3,5,7]
print(remove_duplicates(arr))
