from typing import List


#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by their start times
        intervals.sort(key= lambda x:x[0])

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True




        


a = Solution()
intervals = [(5,8),(9,15)]

#intervals = [(0,30),(5,10),(15,20)]
print(a.canAttendMeetings(intervals))
