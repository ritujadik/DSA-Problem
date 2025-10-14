"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

"""
def square_of_sorted_array(x):
    result = []
    for i in x:
        result.append(i*i)

    return sorted(result)



x = [-4,-1,0,3,10]
print(square_of_sorted_array(x))