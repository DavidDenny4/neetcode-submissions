class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(amount):
            
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1

            if amount in cache:
                return cache[amount]
            
            lowest = float('inf')
            for coin in coins:
                result = dfs(amount - coin)
                if result != -1:
                    lowest = min(lowest, 1 + result)

            if lowest == float('inf'):
                cache[amount] = -1
            else:
                cache[amount] = lowest
            return cache[amount]
        
        return dfs(amount) 

        

                

