class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(amount):
            
            if amount == 0:
                return 0
            
            if amount < 0:
                return None
            
            lowest = float('inf')
            for coin in coins:
                result = dfs(amount - coin)
                if result == -1:
                    continue
                lowest = min(lowest, 1 + result)

            return lowest if lowest != float('inf') else -1
        
        return dfs(amount) 

        

                

