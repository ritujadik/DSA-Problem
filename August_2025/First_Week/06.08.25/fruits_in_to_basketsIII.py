def fruits_into_baskets(fruits,baskets):
    n = len(fruits)
    count = 0
    used = [False] * n

    for i in range(n):
        for j in range(n):
            if not used[j] and baskets[j] >= fruits[i]:
                used[j] = True
                break
        else:
            count += 1
    return count





fruits = [4,2,5]
baskets = [3,5,1]
print(fruits_into_baskets(fruits,baskets))
