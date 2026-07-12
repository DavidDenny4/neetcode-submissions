"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        S, E = 0, 0
        max_count, count = 0, 0
        start.sort()
        end.sort()
        while S < len(start):
            if start[S] < end[E]:
                count += 1
                S += 1
            else:
                count -= 1
                E += 1
            max_count = max(max_count, count)
        return max_count
