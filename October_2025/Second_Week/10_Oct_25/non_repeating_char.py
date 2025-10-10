"""
write a function to find the first non repeating character in string
"""
# it is a first apporoach but the time complexity is high in this
# def non_repeating_char(x):
#     for i in range(len(x)):
#         if x[i] not in x[i+1:]:
#             return x[i]


# second approach
def non_repeating_char(x):
    count_dict = {}
    for i in x:
        count_dict[i] = count_dict.get(i,0)+1

    for i in x:
        if count_dict[i] == 1:
            return i

    return None


x = "abaddc"
print(non_repeating_char(x))


