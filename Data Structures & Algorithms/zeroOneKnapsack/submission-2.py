class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = [[0] * len(profit) for i in range(capacity)]
        print(f"the cache looks like {cache}")


        return 0