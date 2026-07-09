def maxProfit(prices):
    maxProfit=0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit=prices[j]=prices[i]
            if profit>maxProfit:
                maxProfit=profit
    return maxProfit