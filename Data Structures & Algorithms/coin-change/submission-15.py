class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def combinations(index, total, count, fewest_number):

            if index >= len(coins) or total > amount:
                return fewest_number
            
            total += coins[index]
            count += 1
            print(f"total is {total} and count is {count} and index is {index} and few is {fewest_number}")
            if total == amount:
                if fewest_number == -1:
                    return count
                fewest_number = min(fewest_number, count)
                return fewest_number

            combinations(index + 1, total, count, fewest_number)
            total -= coins[index]
            count -= 1
            combinations(index + 1, total, count, fewest_number)
            combinations(index, total, count, fewest_number)

        fewest = combinations(0, 0, 0, -1)
        return

