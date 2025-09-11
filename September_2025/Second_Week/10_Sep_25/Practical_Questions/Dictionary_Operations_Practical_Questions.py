# Add two dictionary or merging two dictionary
# Ist way
# def add_dict(d1,d2):
#     return {**d1,**d2}

# IInd way
# def add_dict(d1,d2):
#     result = d1.copy()
#     result.update(d2)
#     return result
#
# d1 = {"name":"rituja"}
# d2 = {"age":25}
# print(add_dict(d1,d2))


#a) Insertion of dictionaries by keys
#1. Findout common keys between two dictionaries
# def comman_keys(d1,d2):
#     result = d1.keys() & d2.keys()
#     return result
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 20, 'c': 30, 'd': 40}
#
# print(comman_keys(d1,d2))

#2. Findout common items between two dictionaries
# def comman_items(d1,d2):
#     result = d1.items() & d2.items()
#     return result
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(comman_items(d1,d2))

#b) Difference between dictionaries
# keys in d1 but not in d2
def diff_keys(d1,d2):
    result = d1.keys() - d2.keys()
    return result

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(diff_keys(d1,d2))

#Items in d1 but not in d2
# def diff_items(d1,d2):
#     result = d1.items() - d2.items()
#     return result
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(diff_items(d1,d2))


#Checking for subset/superset
# def is_subset(d1,d2):
#     result = d1.items()<=d2.items()
#     return result
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(is_subset(d1,d2))

# def is_superset(d1,d2):
#     result = d2.items()>=d1.items()
#     return result
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(is_superset(d1,d2))

#Combining value of same keys
# add values of common keys
# from collections import Counter
# def add_value_of_common_keys(d1,d2):
#     result = dict(Counter(d1) + Counter(d2))
#     return result
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# print(add_value_of_common_keys(d1,d2))

#Looping Through two dicts Simultaneously
# def loops_two_dict(d1,d2):
#     for keys in d1:
#         if keys in d2:
#             print(f"{keys}:{d1[keys]} vs {d2[keys]}")
#
# d1 = {'a': 1, 'b': 8, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
#
# loops_two_dict(d1,d2)

# filtering in dictionary
# def filter_keys(d1,d2):
#     result = [k for k in d1 if k in d2 and d1[k] !=d2[k]]
#     return result
#
#
# d1 = {'a': 1, 'b': 8, 'c': 3}
# d2 = {'b': 2, 'c': 30, 'd': 40}
# print(filter_keys(d1,d2))

# Zipping two dictionary together
def zipped_two_dict(d1,d2):
    zipped = {k: (d1[k],d2[k]) for k in d1.keys() & d2.keys()}
    return zipped

d1 = {'a': 1, 'b': 8, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 40}
print(zipped_two_dict(d1,d2))





