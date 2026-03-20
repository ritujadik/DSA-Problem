def reverse_arr_grp(arr,k):
    new_arr = []
    for i in range(0,len(arr),k):
        grp = arr[i:i+k]
        new_arr.extend(grp[::-1])

    return new_arr


arr = [4,2,8,9,6,4,3]
print(reverse_arr_grp(arr,3))