def subarray_sum(arr,k):
    new_arr = []
    for i in range(len(arr)):
        total = 0
        for j in range(i,len(arr)):
            total += arr[j]

            if total == k:
                new_arr.append(arr[i:j+1])

    return set(new_arr)


arr = [1,1,1,-1]
k = 2
print(subarray_sum(arr,k))
