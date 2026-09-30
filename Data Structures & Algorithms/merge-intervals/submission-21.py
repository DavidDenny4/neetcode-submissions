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
                # print(f"we are in the else")
                start = min(intervals[i - 1][0], intervals[i][0])
                end = max(intervals[i - 1][1], intervals[i][1])
                # print(f"start is {start} and end is {end}")
                intervals[i] = [start,end]
                # print(f"intervals is now {intervals}")
            
        res.append(intervals[i - 1])
        return res

            

    