class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            while nums[R] < nums[L]:
                profit = max(profit,nums[R] - nums[L])
                L = R
                R += 1
        return profit

            
            