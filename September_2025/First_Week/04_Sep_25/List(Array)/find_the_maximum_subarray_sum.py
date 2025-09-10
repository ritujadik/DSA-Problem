def max_subarray_sum(x):
    max_ending_here = max_so_far = x[0]

    for num in x[1:]:
        max_ending_here = max(num,max_ending_here+num)
        max_so_far = max(max_so_far,max_ending_here)

    return max_so_far


x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(x))