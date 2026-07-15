class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            while prices[R] < prices[L]:
                profit = max(profit,prices[R] - prices[L])
                L = R
                R += 1
        return profit

            
            