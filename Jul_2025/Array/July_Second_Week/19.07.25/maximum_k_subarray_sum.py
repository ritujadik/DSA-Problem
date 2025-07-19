#Given an array and a number k, find the sum of the subarray that has the maximum sum among all the subarrays of size k.

def maximum_k_subarray_sum(x,k):
    left = 0
    n = len(x)
    new_sub_array = []
    current_sum = sum(x[:k])
    new_sub_array.append(current_sum)

    for right in range(k,n):
         current_sum+= x[right]-x[left]
         left+=1
         new_sub_array.append(current_sum)
    return max(new_sub_array)


x = [3, 5, 6, 2, 4, 7, 8]
k = 3
print(maximum_k_subarray_sum(x,k))