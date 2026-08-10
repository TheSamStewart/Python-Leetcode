class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Copy and Paste into comments:

        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Need to insert the new interval into intervals such that the ascending order is still kept.

        [4,8]

        [[1,2],[3,5],[6,7],[8,10],[12,16]]
                  

        [[1,2],[3,10],[12,16]]


        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        Two pointer solution that uses while loop.

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        First we iterate until we find newInterval[0] >= interval[i], copying the array at each stage 

        while newInterval[0] < interval[i][j]

        When we find the point in the intervals array where newInterval[0] >= interval[i] we now ignore all elements in the array until we find newInterval[1] <= interval[i] then we start copying again

        while newInterval[1] >= interval[i][j] 


        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible. 

        '''


        res = []
        i = 0
        n = len(intervals)

        #Append intervals until we find an interval where newInterval fits
        #Position for new interval has to live after intervals[i][1]

        while i < n and intervals[i][1] < newInterval[0]:

            res.append(intervals[i])
            i += 1

        #Compare the newIntervals with new intervals, we keep the smallest and largest from both until we cant merge further 

        while i < n and intervals[i][0] <= newInterval[1]:

            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])

            i += 1

        res.append(newInterval)

        #Then append the rest for the final result

        while i < n:

            res.append(intervals[i])

            i += 1

        return res
