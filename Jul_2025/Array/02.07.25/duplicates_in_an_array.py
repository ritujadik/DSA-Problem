# find the duplicates in an array
def duplicate_in_array(x):
    new_dic = {}
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[j] == x[i]:
                if x[i] in new_dic:
                    new_dic[x[i]] +=1
                else:
                    new_dic[x[i]] = 2

    return new_dic


x = ['a','b','a','c','a','b','d','b']
print(duplicate_in_array(x))