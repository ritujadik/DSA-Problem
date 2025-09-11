# How do you create a dictionary?
d = {'a': 1,'b': 6}

# how do you access a value of dictionary
print(d['a'])

# how do we access a key without risking an error?
print(d.get('b'))

# How do we add or update key value pairs?

d['c'] = 3
d['a'] = 10

print(d)

# how do we remove a key-value pair?
val = d.pop('b')
print(val)

# How do we iterate on keys,values or both
for key in d:
    print(key)

for vall in d.values():
    print(vall)

for valll in d.items():
    print(valll)

# how do we check if a key exists
print('a' in d)

# how do we merge two dictionary
d1 = {'a': 1}
d2 = {'b': 2}
print(d1 | d2)

# how do create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys,values))
print(d)

# how do handle default values when accessing keys(like counting freq)
freq = {}
for i in "Rajababu":
    freq[i] = freq.get(i,0) + 1
print(freq)


