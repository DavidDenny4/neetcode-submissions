class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def combinations(index, total, count, ):

            if total == amount:
                fewest_number = min(fewest_number, count, fewest_number)
                return
            
            if index >= len(coins) or total > amount:
                return
            
            total += coins[index]
            count += 1
            combinations(index + 1, total, count, fewest_number)
            total -= coins[index]
            count -= 1
            combinations(index + 1, total, count, fewest_number)

        fewest = combinations(0, 0, 0, len(coins) + 1)

        return fewest if fewest != len(coins) + 1 else -1

