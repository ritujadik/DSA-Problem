# How do you create a tuple
t = (1,2,3)
print(t)

# how do you access element in a tuple
print(t[0])
print(t[1])

# how do we concatenate two tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# how do we repeat a tuple multiple times
t = (1,2,3)
print(t*3)

# how do we unpack a tuple
t = (1,2,3)
a,b,c = t
print(a,b,c)

# how do we check if an element exist in tuple?
t = (1,2,3)
print(2 in t)

# can tuples contain mutuable elements
t = ([1,2,3],4,5)
t[0].append(9)
print(t)

# how do you convert a list in tuple and tuple in list
x = [1,2,3]
print(tuple(x))
y = (4,3,9)
print(list(y))
