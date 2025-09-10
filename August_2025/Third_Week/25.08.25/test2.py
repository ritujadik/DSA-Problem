def add_dict(d1,d2):
    result = list(d1.items())+ list(d2.items())
    return result




d1 = {'name':'ritu'}
d2 = {'dept':'development'}

print(add_dict(d1,d2))


