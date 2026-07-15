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

        intervals.sort()
        for index in range(len(intervals) - 1):
            curr_start = intervals[index].start
            curr_end = intervals[index].end
            next_start = intervals[index + 1].start
            next_end = intervals[index + 1].end

            if next_start < curr_end or next_end > curr_start:
                return False
        return True

