class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = [[0 for i in range(len(profit) + 1)] for i in range(capacity + 1)]
        print(f"the cache looks like {cache}")

        return 0