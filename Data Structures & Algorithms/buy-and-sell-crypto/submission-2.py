class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            profit = max(profit, prices[R] - prices[L])
            if prices[R] > prices[L]:
                L = R
        return profit

            
            