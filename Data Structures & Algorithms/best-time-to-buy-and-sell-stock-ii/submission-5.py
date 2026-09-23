class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                profit += (prices[i - 1] - curr)
                curr = prices[i]
        profit += prices[len(prices) - 1] - curr
        return profit