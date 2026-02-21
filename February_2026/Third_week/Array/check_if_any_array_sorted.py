def arraySort(arr):
    new_arr = []
    prev_elem = arr[0]
    new_arr.append(prev_elem)
    for i in arr[1:]:
        if i>=prev_elem:
            new_arr.append(i)
            prev_elem = i
        else:
            new_arr.append(prev_elem)

    if arr == new_arr:
        return True
    else:
        return False

arr = [1,2,3,4,5]
print(arraySort(arr))