"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            nextStart = intervals[i].start
            nextEnd = intervals[i].end

            if end > nextStart:
                return False
            else:
                start = nextStart
                end = nextEnd

        return True