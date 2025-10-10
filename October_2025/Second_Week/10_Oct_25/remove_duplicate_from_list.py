"""
write a function to remove duplicate from the list while preserving the order of elements

"""

def remove_a_duplicate(x):
    seen = set()
    result = []
    for i in x:
        if i not in seen:
            result.append(i)
            seen.add(i)

    return result



x = [1,3,2,3,5,6,5]
print(remove_a_duplicate(x))
