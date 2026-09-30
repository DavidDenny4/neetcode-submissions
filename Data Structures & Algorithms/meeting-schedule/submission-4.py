"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda x: x.start)
        for index in range(1, len(intervals) - 1):
            curr_start = intervals[index].start
            curr_end = intervals[index].end
            prev_start = intervals[index - 1].start
            prev_end = intervals[index -1 ].end

            if curr_start >= prev_end:
                continue
            if curr_end <= prev_start:
                continue
            return False


        return True

