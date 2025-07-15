"""Given an array and a number k, remove all occurrences of k from the array (in-place). Return the number of elements 'remainingSize' left after removing k. Note that removing the occurences is mandatory and will be checked in the main method. There can be anything beyond the first 'remainingSize' elements. It will be ignored.

Example"""

def remove_occurence(x,k):
    left = 0
    right = len(x)-1
    while left<=right:
        if x[left] == k:
            x.pop(left)
            right-=1
        elif x[right] ==k:
            x.pop(right)
            right-=1
        else:left+=1
    return len(x)



# def remove_occurence(x,k):
#     for i in x:
#         if i == k:
#             x.pop(i)
#     return len(x)




x = [1,2,3,4,5,6,7,4,8,4]
k = 4
print(remove_occurence(x,k))
