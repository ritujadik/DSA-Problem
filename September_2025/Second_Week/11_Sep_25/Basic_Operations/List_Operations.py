# Add two list
l1 = [1,3,4]
l2 = [4,5,6]

print(l1 + l2)

# Subtract two list
l1 = [1,3,4]
l2 = [4,5,6]
result = [i for i in l1 if i not in l2]
print(result)

# reverse a list in python
l1 = [2,4,6,7]
l1_new = l1[::-1]
print(l1_new)

# remove duplicates from a list
l1 = [1,2,3,4,3,2,1,5]
print(list(set(l1)))

# find the frequency of each element in a list
l1 = [1,2,3,4,3,2,1,5]
freq = {}
for item in l1:
    if item in freq:
        freq[item] +=1
    else:
        freq[item] = 1
print(freq)


# find the largest and smallest element in the list
l1 = [1,2,3,4,3,2,1,5]
print(max(l1))
print(min(l1))
# by loop
max_elem = l1[0]
min_elem = l1[0]
for num in l1:
    if num>max_elem:
        max_elem = num

    if num<min_elem:
        min_elem = num

print("max_elem",max_elem)
print("min_elem",min_elem)


# How do you sort a list in Python?
l = [5,2,9,1,5,6]
l.sort()
print(l)

# how do you check if the element exist in a list
l1 = [1,2,3,4,3,2,1,5]
print(5 in l1)

# how do you copy a list in python without affecting a original
orignal = [1,2,3]
copy1 = list(orignal)
print(copy1)

# how do you remove a element from a list in python
l = [10,20,30,40]
l.remove(30)
print(l)

# How do you enumerate over a list with both index and value
l = ['a','b','c']
for index,value in enumerate(l):
    print(f"index:{index} and value:{value}")