class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                profit += (prices[i - 1] - curr)
                curr = prices[i]
            print(f"curr is now {curr} and i is {i}")
        return profit