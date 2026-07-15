# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(1, len(pairs)):
            m = i - 1
            while m >=0 and pairs[m + 1].key < pairs[m].key:
                temp = pairs[m]
                pairs[m] = pairs[m + 1]
                pairs[m + 1] = temp
                m -= 1
            res.append(pairs)
        return res
