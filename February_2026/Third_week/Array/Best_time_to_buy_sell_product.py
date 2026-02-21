def max_profit(nums):
    max_profit = 0
    min_price = float('inf')

    for i in nums:
        min_price = min(min_price,i)
        profit = i-min_price
        max_profit = max(max_profit,profit)

    return max_profit



x = [3,2,4,1,8,9,7,6]
print(max_profit(x))