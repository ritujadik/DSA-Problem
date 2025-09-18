def two_sum(x,k):
    left = 0
    right = len(x)-1
    new_list = []
    while left<right:
        total = x[left] + x[right]
        if total == k:
            new_list.append((left,right))
            left+=1
            right-=1

        elif total<k:
            left+=1

        else:
            right-=1


    return new_list



x= [1,2,4,3,5,6]
k = 7
print(two_sum(x,k))
