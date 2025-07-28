"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Ex- 123 should be 321
    -123 should be -321
    120 should be 21
"""
#Approach
# 1. We have to take number
# 2. divide bye 3
# 3. remainder will take and multiply by 10 also add one variable whose intial value would be 0
# 4. will do untill the last value and added the same in result variable
# 5. return result

def reverse_number(x):
    result = 0
    x = int(x)
    sign = 1 if x >0 else -1
    x = abs(x)
    while x !=0:
        new_temp = x % 10
        result = result * 10 + new_temp
        x = x // 10
    result = result * sign
    if result > -2**31 or result > 2**31-1:
        return 0
    return result



x = 1534236469
print(reverse_number(x))