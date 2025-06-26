# Write a Python function that takes a list of numbers and returns the largest one.
def largest_number(li):
    max_num = li[0]
    for i in li:
        if i > max_num:
            max_num = i
    return max_num

li = [2,3,4,5,9,10]
print(largest_number(li))