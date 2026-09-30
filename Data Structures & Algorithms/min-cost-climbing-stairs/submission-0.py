class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1 for i in range(len(cost))]

        def helper(index, price):
            if index >= len(cost):
                return 0
            
            price += cost[index]
            one_jump = helper(index + 1, price)
            two_jump = helper(index + 2, price)
            cache[index] = min(one_jump, two_jump)

            return cache[index] 
            
        return min(helper(0,0), helper(1,0))