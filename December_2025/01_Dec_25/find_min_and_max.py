# find the minimum and maximum in an array

# def min_and_max(x):
#     min_elem = min(x)
#     max_elem = max(x)
#     return("min_elem",{min_elem},"max_elem",{max_elem})
#
#
# x = [3,1,4,1,5,9]
# print(min_and_max(x))


# check if array is sorted
# def sorted_array(x):
#     if x == sorted(x):
#         return True
#     else:
#         return False
#
# x = [5,2,3,4]
# print(sorted_array(x))

# Find the Second Largest Element in an array
# def second_largest_elem(x):
#     x_new = sorted(x)
#     return x_new[-2]
#
#
# x = [10,20,4,45,99]
# print(second_largest_elem(x))

# Reverse an Array in place
# def reverse_array(x):
#     result = x[::-1]
#     return result
#
# x = [1,2,3,4]
# print(reverse_array(x))

# Move all the zeros to the end
def move_zeros_to_the_end(x):
    n = len(x)
    j = 0
    for i in range(n):
        if x[i] != 0:
            x[j] = x[i]
            j += 1
    for k in range(j,n):
        x[k] = 0
    return x

x = [0,1,0,3,12]
print(move_zeros_to_the_end(x))



