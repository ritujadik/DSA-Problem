# def max_element(x):
#     left = 0
#     right = len(x)-1
#     max_elem = x[0]
#     while left <= right:
#         if x[left]>max_elem:
#             max_elem = x[left]
#
#         if x[right]>max_elem:
#             max_elem = x[right]
#
#         left+=1
#         right-=1
#     return max_elem

def min_element(x):
    left = 0
    right = len(x)-1
    min_elem = x[0]

    while left<=right:
        if x[left]<min_elem:
            min_elem = x[left]

        if x[right]<min_elem:
            min_elem = x[right]
        left+=1
        right-=1
    return min_elem




x = [2,3,7,9,5,4]
print(min_element(x))