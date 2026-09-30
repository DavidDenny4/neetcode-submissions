class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        len_p, len_w = len(profit), len(weight)
        cache = [[0] * len_p for i in range(len_w)]

        print(f"the cache looks like {cache}")


        return 0