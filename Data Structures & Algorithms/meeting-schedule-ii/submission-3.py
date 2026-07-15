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
        count = 0
        start.sort()
        end.sort()
        print(f"start is {start} and end is {end}")
        while S < len(start):
            if start[S] < end[E]:
                count += 1
                S += 1
            else:
                count -= 1
                E += 1
            print(f"count is now {count}")
        return count
