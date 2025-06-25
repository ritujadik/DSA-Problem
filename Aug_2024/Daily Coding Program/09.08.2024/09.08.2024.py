def nestedarray(arr):
    result = []
    for i in arr:
        if type(i) == list:
            result = result + nestedarray(i)
        elif type(i) == int:
                result.append(i)
    return result




arr = ['a',2,'b',['c',5],[6,[7,8,9]]]
x = nestedarray(arr)
print(x)
