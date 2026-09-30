class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for index in range(len(intervals)):
            if newInterval[0] > intervals[index][1]:
                print(f"appending {intervals[index]}")
                res.append(intervals[index])
            elif newInterval[1] < intervals[index][0]:
                res.append([newInterval])
            else:
                min_start = min(newInterval[0], intervals[index][0])
                max_end = max(newInterval[1], intervals[index][1])

        return res