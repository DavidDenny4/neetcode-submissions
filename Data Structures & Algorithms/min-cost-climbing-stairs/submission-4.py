class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1 for i in range(len(cost))]

        def helper(index):
            if index >= len(cost):
                return 0
            
            if cache[index] != -1:
                return cache[index]

            cache[index] = cost[index] + min(helper(index + 1), helper(index + 2))
            return cache[index] 
            
        return min(helper(0), helper(1))