class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            print(f"prev is {prev}")
            print(f"i is {i} and intervals at i is {intervals[i]}")
            if intervals[i][0] > prev[1]:
                res.append(prev)
                prev = intervals[i]
            else:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
        res.append(prev)
        return res