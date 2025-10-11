"""
write a factorial of a given number
"""
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)


x = 5
print(factorial(x))