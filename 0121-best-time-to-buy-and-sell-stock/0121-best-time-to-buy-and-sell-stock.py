class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = float('inf')

        for i in prices:
            if i<low:
                low = i
            profit = i-low
            if profit > max_profit:
                max_profit = profit
        return max_profit 

       
        