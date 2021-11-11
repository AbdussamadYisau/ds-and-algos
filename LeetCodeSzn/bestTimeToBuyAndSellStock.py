class Solution:
    def maxProfit(prices):
        minValue = float('+inf')
        maxProfit = 0
        
        for i in range(len(prices)):
            
            if prices[i] < minValue:
                minValue=prices[i]
            
            maxProfit = max(maxProfit, prices[i] - minValue)
        
        return maxProfit
    
    def maxProfitPointers(prices):
        l = 0
        r = 1
        maxProfit = 0


        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: 
                l = r
            r += 1
        return maxProfit

print(Solution.maxProfitPointers([7,1,5,3,6,4]))