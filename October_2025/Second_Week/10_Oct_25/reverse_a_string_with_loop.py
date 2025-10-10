"""
reverse a string using loop or stack
"""

# loop approach

# def reverse_a_string(x):
#     x_new = []
#     for i in range(len(x)-1,-1,-1):
#             x_new.append(x[i])
#     return x_new

# stack approach
def reverse_a_string(x):
    new_list = []
    for i in x:
        new_list.append(i)

    x_new = []
    while new_list:
        x_new.append(new_list.pop())

    return x_new


x = ['a','w','v','i']
print(reverse_a_string(x))
