# x = "Sita is a Ram's wife"
# x1 = " ".join(x.split()[::-1])
# x2 = x[::-1]
# print(x1)
#
#
#
#
#
#
# def split_at_same_position(x):
#     word = ''
#     result = []
#     # x_new = ' '.join((x.split()))
#     for i in x:
#         if i!= ' ':
#             word+=i
#         else:
#             result.append(word[::-1])
#             result.append(' ')
#             word = ' '
#     if word:
#         result.append(word[::-1])
#     return ' '.join(result)
#
#
# x = "Sita is a Ram's wife"
# print(split_at_same_position(x))
#
# name = "Rituja Dikshit"
# def check_vowels(x):
#     x = x.lower()
#     count = 0
#     for i in x:
#         if i  not in ['a','e','i','o','u']:
#             count+=1
#     return count
#
# x = "Rituja Dikshita"
# print(check_vowels(x))

# def all_characters_are_unique(x):
#     x = x.lower()
#     for i in range(len(x)):
#         if x[i] in x[i+1:]:
#             print("this string has not all unqiue letters")
#             return
#     else:
#         print("this string has all the unique letters")
#
#
# x = "Rituja"
# all_characters_are_unique(x)

# def check_anagram(s1,s2):
#     s1 = s1.replace(" ","").lower()
#     s2 = s2.replace(" ","").lower()
#     return sorted(s1) == sorted(s2)
#
# extract digit
# text = "a1b2c3"
# #output = [1,2,3]
# digits = [int(i) for i in text if i.isdigit()]
# print(digits)
x = ['a','b','c']
indexed = [(i,val) for i,val in enumerate(x)]
print(indexed)
