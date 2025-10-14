"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
def nums_even_digit(x):
    count = 0
    for i in x:
        if len(str(i)) % 2 == 0:
            count+=1

    return count


x = [12,345,2,6,7896]
print(nums_even_digit(x))





