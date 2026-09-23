class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = [[-1 for i in range(len(profit))] for i in range(capacity + 1)]

        def helper(cap, index):
            if index == len(profit):
                return 0

            if cache[cap][index] != -1:
                return cache[cap][index]
            
            cache[cap][index] = helper(cap, index + 1)
            if (cap - weight[index]) >= 0:
                p = profit[index] + helper(cap - weight[index], index + 1)
                cache[cap][index] = max(cache[cap][index], p)
            
            return cache[cap][index]
        
        return helper(capacity, 0)