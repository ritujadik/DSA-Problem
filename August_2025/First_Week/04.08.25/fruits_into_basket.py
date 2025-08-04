def fruit_basket(x):
    start = 0
    max_fruit = 0
    basket = {}
    for i in range(len(x)):
        basket[x[i]] = basket.get(x[i],0) + 1
        while len(basket)>2:
            basket[x[start]]-=1
            if basket[x[start]] == 0:
                del basket[x[start]]
            start+=1

        max_fruit = max(max_fruit,i-start+1)

    return max_fruit





x = [1,2,3,2,2]
print(fruit_basket(x))
