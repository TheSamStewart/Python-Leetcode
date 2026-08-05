"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        U - We need to sort the list and merge all intervals 
        M - Array's, sorting
        P -
        '''
        
        #Iterate through the array of intervals and create array then sort

        start = []
        end = []
        count = 0
        max_count = 0

        for interval in intervals:

            start_time = interval.start
            end_time = interval.end 

            start.append(start_time)
            end.append(end_time)

        start.sort()
        end.sort()

        s = 0
        e = 0

        while s < len(intervals) and e < len(intervals):

            if start[s] < end[e]:

                count += 1

                max_count = max(count, max_count)

                s += 1

                continue

            e += 1

            count -= 1  

        return max_count



        





        
