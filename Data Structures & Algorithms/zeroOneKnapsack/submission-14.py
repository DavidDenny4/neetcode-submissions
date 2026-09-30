class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = [[0 for i in range(len(profit))] for i in range(capacity + 1)]

        # Set profit 0 if capcity is less than weight of item 1
        for i in range(len(cache)):
            if weight[0] <= i:
                cache[i][0] = profit[0]

        for capacity in range(1, len(cache)):
            for item in range(1, len(cache[0])):
                skip = cache[capacity][item - 1]
                include = 0
                if (capacity - weight[item]) >= 0:
                    include = profit[item] + cache[capacity - weight[item]][item - 1]
                    cache[capacity][item] = max(skip, include)
                
        return cache[capacity][len(profit) - 1]

        