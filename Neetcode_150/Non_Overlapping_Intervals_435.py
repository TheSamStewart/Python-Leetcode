class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #sort by the end interval, this ensures we keep the most unoverlapping intervals (min removals).

        intervals.sort(key = lambda x:x[1])

        n = len(intervals)
        i = 0

        res = 0

        for current in intervals[1:]:

            prev = intervals[i]

            #this is an overlap

            if current[0] < prev[1]:

                #mark current as removed 

                current[0] = 'R'

                res += 1

                continue

            i += 1

            while intervals[i][0] == 'R' and i < n:

                i += 1

        return res


            

 



        


        
