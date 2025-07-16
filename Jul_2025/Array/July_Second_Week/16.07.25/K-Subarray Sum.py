# Given an array and a number k, find the sum of all the subarrays of size k.
def k_subarray_sum(x,k):
    new_subarray_sum = []
    n = len(x)
    left = 0

    current_sum = sum(x[:k])
    new_subarray_sum.append(current_sum)

    for right in range(k,n):
        current_sum += x[right]-x[left]
        left+=1
        new_subarray_sum.append(current_sum)

    return new_subarray_sum

x = [3, 5, 6, 2, 4, 7, 8]
k = 3
print(k_subarray_sum(x,k))