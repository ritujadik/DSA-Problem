def three_sum(x):
    x_new = list(enumerate(x))
    x_new.sort(key=lambda pairs:pairs[1])

    result = []
    n = len(x_new)

    for i in range(n-2):
        if i>0 and x_new[i][1] == x_new[i-1][1]:
            continue
        left = i+1
        right = n-1

        while left < right:
            current_sum = x_new[i][1]+x_new[left][1] +x_new[right][1]
            if current_sum == 0:
                triplet =  x_new[i][1],x_new[left][1],x_new[right][1]
                result.append(triplet)

                while left<right and x_new[left][1] == x_new[left+1][1]:
                    left+=1
                while left<right and x_new[right][1] == x_new[right-1][1]:
                    right-=1
                left+=1
                right-=1

            elif current_sum<0:
                left+=1
            else:right-=1


    return result

x = [-1,0,1,2,-1,-4]
print(three_sum(x))