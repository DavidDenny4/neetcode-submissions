class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0
        for R in range(1, len(prices) - 1):
            if prices[R] - prices[L] > 0:
                profit += prices[R] - prices[L]
                L = R
        return profit