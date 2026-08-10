"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Sort the data by the start data, this optimizes the search for overlaps

        intervals.sort(key = lambda x : x.start)

        #Iterate through the data checking for overlaps, if an overlap appears  return false

        for i in range(len(intervals)-1):

            if intervals[i].end > intervals[i+1].start:

                return False

        return True
