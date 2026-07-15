class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        start, end = newInterval[0], newInterval[1]
        for index in range(len(intervals)):
            if start > intervals[index][1]:
                res.append(intervals[index])
            elif end < intervals[index][0]:
                res.append([start, end])
            else:
                start = min(start, intervals[index][0])
                end = max(end, intervals[index][1])


        return res