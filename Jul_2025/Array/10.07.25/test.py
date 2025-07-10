# #4.	Create a generator function that reads a large file line by line instead of loading entire file into memory.
# import os
# def readfile(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             for line in file:
#                 yield line.strip()
#     except FileNotFoundError:
#         print(f"File not found: {filename}")
#     except IOError as e:
#         print(f"I/O error({e.errno}): {e.strerror}")
#     except Exception as e:
#         print(f"Unexpected error: {str(e)}")
#
# print("current director:")
# print(os.getcwd())
#
# filename = "Split_the_array.py"
# if os.path.isfile(filename):
#     print(f"\n Reading contents of: {filename}\n")
#     for line in readfile(filename):
#         print(line)
# else:
#     print(f"\n File '{filename}' does not exist")
#
# #4.	Write a generator that mimics Python’s range(start, stop, step)
#
# def customrange(start,stop,step):
#     while start<stop:
#         yield start
#         start+=step
#
#
# customrange(3,6,1)
# print(list(customrange(3,6,1)))

# Prime number generator
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True
#
# def prime_generator(limit):
#     count,num = 0,2
#     while count<limit:
#         if is_prime(num):
#             yield num
#             count+=1
#         num+=1
#
#
# print(list(prime_generator(8)))

def alternate_gen(list1,list2):
    for a,b in zip(list1,list2):
        yield a
        yield b


print(list(alternate_gen([2,3,4],[5,6,7])))