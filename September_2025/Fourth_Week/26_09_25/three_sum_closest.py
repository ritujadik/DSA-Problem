def three_sum_closest(x,k):
    x.sort()
    n = len(x)
    closest_sum = float("inf")
    for i in range(n-2):
        left = i+1
        right = n-1
        while left<right:
            current_sum = x[left] + x[right] + x[i]
            if abs(current_sum-k) < abs(closest_sum-k):
                closest_sum = current_sum

            if current_sum<k:
                left+=1

            elif current_sum>k:
                right-=1

            else:
                return k

    return closest_sum




x = [-1,2,1,-4]
k = 1
print(three_sum_closest(x,k))

