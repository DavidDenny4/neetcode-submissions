class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        print(f"intervals sorted is now {intervals} and for loop si {len(intervals) - 1}")
        for i in range(len(intervals) - 1):
            print(f"i is {i}")
            if intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])
            else:
                print(f"this is else {intervals[i]}")
                start = min(intervals[i][0], intervals[i + 1][0])
                end = max(intervals[i][1], intervals[i + 1][1])
                intervals[i + 1][0], intervals[i + 1][1] = start, end
                i += 2
        return res

    