def move_zero(arr):
    insert_post = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_post],arr[i] = arr[i],arr[insert_post]
            insert_post+=1
    return arr

arr = [1,0,3,2,0,5,0,6,7]
print(move_zero(arr))