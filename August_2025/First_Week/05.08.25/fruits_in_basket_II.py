# def fruits_in_basket(fruits,baskets):
#     baskets.sort()
#
#     count = 0
#     for fruit in fruits:
#         placed = False
#         for i in range(len(baskets)):
#             if baskets[i] >= fruit:  # Try to place the fruit in this basket
#                 baskets[i] = -1  # Mark the basket as used
#                 placed = True
#                 break  # Stop looking for a basket once the fruit is placed
#         if not placed:
#             count += 1
#     return count
#
#
#
#
# x1 = [4,2,5]
# x2 = [3,5,4]
# print(fruits_in_basket(x1,x2))
def fruits_in_basket(fruits, baskets):
    n = len(fruits) and len(baskets)
    count = 0
    x_new = []
    used = [False]*n

    for i in range(n):
        for j in range(n):
            if not used[j] and baskets[j]>=fruits[i]:
                x_new.append(baskets[j])
                used[j] = True
                break
        else:
            count+=1
    return count




# Example usage
x1 = [4, 2, 5]
x2 = [3, 5, 4]
print(fruits_in_basket(x1, x2))  # Output: 1







