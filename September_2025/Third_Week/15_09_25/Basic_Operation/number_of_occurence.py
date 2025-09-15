def num_of_occurence(x):
    result = {}
    for i in x:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result



x = "Rameshashaha"
print(num_of_occurence(x))
