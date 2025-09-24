"""
write a python function to print the first n terms of the fibonacci series
"""

def fibonacci_series(n):
    x1 = 0
    x2 = 1
    for i in range(n):
        print(x1,end= " ")
        x1,x2 = x2,x1+x2


fibonacci_series(5)

"""
write a python function to check if a string is palindrome
"""
def palindorme(x):
    x_reverse = reversed(x)
    if x == x_reverse:
        return "Palindrome number"

    else:
        return "this is not a palindrome number"


"""
write a python function that returns all prime number between 1 and n
"""

def prime_num(n):
    x_new = []
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
            else:
                x_new.append(i)

    return x_new

print(prime_num(10))



"""
write a function to calculate the factorial of a given number
"""

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return  x* factorial(x-1)


print(factorial(3))


"""find the second largest element in the list"""

def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst)>1 else None

lst = [1,2,5,3,2]
print(second_largest(lst))

"""
find the occurence of the element in list
"""
def count_occurence(lst,value):
    return lst.count(value)

lst = [1,2,5,3,2]
print(count_occurence(lst,value=2))


"""
write a function to check if two string are anagram
"""
def are_anagram(str1,str2):
    return sorted(str1) == sorted(str2)


print(are_anagram("listen", "silent"))

