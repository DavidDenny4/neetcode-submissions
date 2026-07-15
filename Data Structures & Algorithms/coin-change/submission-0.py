class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        fewest_number = len(coins) + 1

        def combinations(index, total, count):

            if total == amount:
                fewest_number = min(fewest_number, count)
                return
            
            if index > len(coins):
                return
            
            total += coins[index]
            count += 1
            combinations(index + 1, total, count)
            total -= coins[index]
            count -= 1
            combinations(index + 1, total, count)
        
        combinations(0, 0, 0)

        return fewest_number if fewest_number != len(coins) + 1 else -1

