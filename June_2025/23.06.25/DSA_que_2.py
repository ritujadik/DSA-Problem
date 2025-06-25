#Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

#Note: Stock must be bought before being sold.



def stock_trade(input_prices):
    max_price = 0
    n = len(input_prices)
    for i in range(n):
        for j in range(i+1,n):
            profit = input_prices[j] - input_prices[i]
            if profit > max_price:
                max_price = profit

    return max_price

input_prices = [7,10,1,3,6,9,2]
print(stock_trade(input_prices))




