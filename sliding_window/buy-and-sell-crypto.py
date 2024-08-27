def maxProfit(prices: list[int]) -> int:
    l,r = 0,1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l] 
            maxP = max(maxP,profit)
        else:
            l=r
        r+=1
    
    return maxP
            





# prices = [10,1,5,6,7,1]
prices=[7,6,4,3,1]
prices=[5,1,5,6,7,1,10]

print(maxProfit(prices))