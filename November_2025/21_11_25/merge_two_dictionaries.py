def merge_two_dict(x1, x2):
    new_dict = x1.copy()
    for key,value in x2.items():
        if key in new_dict:
            new_dict[key] +=value
        else:
            new_dict[key] = value


    return new_dict



x1 = {'a':3,'b':5,'c':7}
x2 = {'a': 2,'d':9,'f':4}
print(merge_two_dict(x1,x2))





