"""
intersection of two list in python
"""
def intersection_of_two_list(l1,l2):
    x_new = []
    for i in l1 and l2:
        if i in l1 and i in l2:
            x_new.append(i)

    return x_new




l1 = [1,2,3]
l2 = [2,3,4]
print(intersection_of_two_list(l1,l2))