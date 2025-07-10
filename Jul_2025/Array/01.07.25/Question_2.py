# find the missing number in array
def missing_number(x):
    n = len(x) + 1
    total_sum = n * (n+1) // 2
    actual_sum = 0
    for i in range(len(x)):
        actual_sum +=x[i]
    print(actual_sum)
    print(total_sum)
    return total_sum - actual_sum

x = [1,2,3,4,5,6,7,9]
print(missing_number(x))
