""""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.
"""

def indices_to_string(x,ind):
    # result = [''] * len(x)
    # for i,c in enumerate(x):
    #     result[ind[i]] = c
    # return ''.join(result)
    new_list = [''] * len(x)
    for i in range(len(x)):
        new_list[ind[i]] = x[i]

    return ''.join(new_list)










x = "codeleet"
ind = [4,5,6,7,0,2,1,3]
print(indices_to_string(x,ind))