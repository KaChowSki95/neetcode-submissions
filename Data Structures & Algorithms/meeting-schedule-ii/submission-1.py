"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = 0
        e = 0
        temp = 0
        ans = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                temp += 1
            else:
                e += 1
                temp -= 1
            ans = max(ans, temp)
        return ans 