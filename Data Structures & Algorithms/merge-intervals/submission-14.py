class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):

            if intervals[i][0] > intervals[i - 1][1]:
                res.append(intervals[i])
            else:
                start = min(intervals[i - 1][0], intervals[i][0])
                end = max(intervals[i - 1][1], intervals[i][1])
                intervals[i][0], intervals[i][1] = start, end
            
        res.append(intervals[i - 1])
        return res

            

    