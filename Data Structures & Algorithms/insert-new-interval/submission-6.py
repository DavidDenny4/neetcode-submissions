class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for index in range(len(intervals)):
            if newInterval[0] > intervals[index][1]:
                res.append(intervals[index])
            elif newInterval[1] < intervals[index][0]:
                res.append([newInterval])
            else:
                newInterval[0] = min(newInterval[0], intervals[index][0])
                newInterval[1] = max(newInterval[1], intervals[index][1])
        res.append(newInterval)
        return res