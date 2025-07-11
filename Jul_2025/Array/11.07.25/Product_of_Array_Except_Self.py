def product_self(x):
    count_zeros = x.count(0)
    product = 1
    new_list = []
    if count_zeros>1:
        return [0]*len(x)

    for i in range(len(x)):
        if x[i] != 0:
            product = product*x[i]

    for j in range(len(x)):
        if count_zeros == 1:
            if x[j] == 0:
                new_list.append(product)
            else:
                new_list.append(0)
        else:
            new_list.append(product//x[j])
    return new_list



x = [1,2,3,4]
print(product_self(x))