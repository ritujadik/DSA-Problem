def array_rotate_by_kth_position(arr,k):
    n = len(arr)
    k = k%n
    return arr[-k:] + arr[:-k]


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(array_rotate_by_kth_position(arr,k))