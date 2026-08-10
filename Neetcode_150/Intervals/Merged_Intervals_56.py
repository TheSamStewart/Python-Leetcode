class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Copy and Paste into comments:

        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Iterate through the intervals checking the merge condition.

        we merge until we cant anymore, at which point interval in array becomes current interval

        merge condition:
        
        if current[1] >= next[0] we can merge: 
            min(current[0], next[0])
            max(current[1], next[1])

        pointers: 

        pointer for interval in array
        pointer for current interval  

        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible.

        '''

        #sort the array so it is in order

        intervals.sort(key = lambda x: x[0])

        #init the merged array with first interval

        merged = [intervals[0]]

        #iterate from next interval (index 1)

        for current in intervals[1:]:

            #get the most recent interval

            prev = merged[-1]

            #if we can merge, merge else: append the current and move on 

            if current[0] <= prev[1]:

                prev[1] = max(prev[1], current[1])

            else:

                merged.append(current)

        return merged


        
        
