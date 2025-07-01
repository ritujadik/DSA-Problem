# find the missing number in array
def missing_number(x):
    n = len(x) + 1
    total_sum = n * (n+1) // 2
    actual_sum = 0
    for i in range(len(x)):
        actual_sum +=x[i]
    return total_sum - actual_sum

x = [1,2,4,5,6,7,8,9]
print(missing_number(x))