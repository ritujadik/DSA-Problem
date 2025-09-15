def fibonacci_series(x):
    result = []
    a,b = 0,1
    for i in range(x+1):
        result.append(a)
        a,b = b, a + b
    return result




print(fibonacci_series(5))


