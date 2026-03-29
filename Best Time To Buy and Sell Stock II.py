class Solution:

    def maxProfit(self, prices):
        max_profit=0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit +=prices[i] - prices[i-1]
        return max_profit


obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
print("-----------------------------")
print(obj.maxProfit([1,2,3,4,5]))
