class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        start, end = newInterval[0], newInterval[1]
        for index in range(len(intervals)):
            if start > intervals[index][1]:
                res.append(intervals[index])
            if end < intervals[index][0]:
                res.append(newInterval)
            else:
                min_start = min(start, intervals[index][0])
                max_end = max(end, intervals[index][1])
                res.append([min_start, max_end])
        return res