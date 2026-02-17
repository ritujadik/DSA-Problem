def frequency_of_char(x):
    new_dict = {}
    count = 1
    for i in x:
        if i in new_dict:
            count += 1
        else:
            count = 1
        new_dict[i] = count

    return new_dict


x = "aabbccccddd"
print(frequency_of_char(x))