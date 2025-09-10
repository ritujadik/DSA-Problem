def missing_number(x):
    sum = 0
    n = len(x)
    for i in x:
        sum = sum+i

    print(sum)

    total_sum = (n+1)*(n+2)//2
    print(total_sum)
    missin_num = total_sum-sum

    return missin_num




x = [1,2,3,4,5,6,7,9]
print(missing_number(x))
