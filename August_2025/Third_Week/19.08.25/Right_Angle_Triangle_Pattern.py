"""1.Right Angle trianlge Pattern"""
# n = 10
# for i in range(1,n+1):
#     print('*' * i)


"""2.Inverted Right Angle Triangle"""
# n = 10
# for i in range(n-1,0,-1):
#     print('*' * i)


"""3.Pyramid Pattern"""
# n = 10
# for i in range(n):
#     print(' ' * (n-i-1) + '*'*(2*i+1))

"""4.Inverted Pyramid"""
# n = 10
# for i in range(n-1,-1,-1):
#     print(' ' * (n-i-1) + '*'*(2*i+1))

"""5.Diamond Pattern"""
# n = 10
# for i in range(n):
#     print(' ' * (n-i-1) + '*' * (2*i+1))
# for i in range(n-2,-1,-1):
#     print(' ' *(n-i-1) + '*' * (2*i+1))


"""6.Number triangle"""
# n=10
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end= ' ')
#     print()

"""7.floyd triangle"""
# n=10
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

# """8.To find prime number till n numbers"""
# def prime_numbers(n):
#     x = []
#     for i in range(2,n+1):
#         is_prime = True
#         for j in range(2,int(i**0.5)+1):
#             if i%j ==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             x.append(i)
#
#     return x
#
#
# print(prime_numbers(20))

""" 9.To find a single occurence of a number in an array"""
# def frequency(x):
#     count = 1
#     result = {}
#     for i in range(len(x)):
#         if x[i] in x[i+1:]:
#             count+=1
#         else:
#             count = 1
#     for item in result:
#         result[item] = count
#
#     return result

# """10.Two Sum"""
# def two_sum(arr,tar):
#     index_new = list(enumerate(arr))
#     index_new.sort(key=lambda pairs:pairs[1])
#     left = 0
#     right = len(arr)-1
#     while left<right:
#         current_sum = index_new[left][1] + index_new[right][1]
#         if current_sum == tar:
#             return index_new[left][0],index_new[right][0]
#         elif current_sum<tar:
#             left+=1
#         else:
#             right-=1
#
#     return None

# """11.Given a string,return the first character that doesnot repeat if all character repeat than return none"""
# def non_repeating_char(x):
#     for i in range(len(x)):
#         if x[i] not in x[:i] and x[i] not in x[i+1:]:
#             return x[i]
#     return None

"""12.Given a strign with the length of longest substring without repeating character"""
def longest_substring(x):
    max_count = 0
    seen = set()
    n = len(x)
    start= 0
    for i in range(n):
        while x[i] in seen:
                seen.remove(x[start])
                start+=1
        seen.add(x[i])
        max_count = max(max_count,i-start+1)

    return max_count







