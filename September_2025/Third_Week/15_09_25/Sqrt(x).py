"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

"""
def sqrt(x):
    result = int(x**0.5)
    return result


x = 8
print(sqrt(x))