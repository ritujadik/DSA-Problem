"""
fibonacci series

"""
def fibonacci_series(x):
    i1 = 0
    i2 = 1
    i_new = []
    i_new.append(i1)
    i_new.append(i2)
    for i in range(2,x):
        sum = i1 + i2
        i1 = i2
        i2 = sum
        i_new.append(sum)

    return i_new


x = 7
print(fibonacci_series(x))


