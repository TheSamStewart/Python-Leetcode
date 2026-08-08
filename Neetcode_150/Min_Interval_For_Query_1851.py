import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Copy and Paste into comments:

        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        res[i] = righti - lefti + 1 where (lefti <= queries[j] and righti >= queries[j]) - this must be the min value where this appears. 

        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        Sort intervals by lefti in ascending order.
        Sort queries in ascending order.

        iterate through queries

        while queries > intervals[lefti]: we push onto the heap

        while heap[0][righti] < query: we pop 

        if heap:

            res[index] = heap[0]

        else:
            
            res[index] = -1

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        When dealing with min values, heap is advisable 

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible. 
        '''

        #init result array len(queries)

        res = [-1] * len(queries)

        #sort intervals by lefti

        intervals.sort(key = lambda x : x[0])

        #for each query in query - store it with its array position for res

        for i, query in enumerate(queries):

            queries[i] = (query, i)

        #sort queries into ascending order

        queries.sort(key = lambda x : x[0])

        #init empty min heap

        min_heap = []

        #pointer for intervals

        j = 0

        #iterate through queries

        for q,i in queries:
               
            #while this is an interval that starts at the correct time for all queries

            while j < len(intervals) and q >= intervals[j][0]:

                size = intervals[j][1] - intervals[j][0] + 1

                heapq.heappush(min_heap, (size, intervals[j][1]))

                j += 1 

            #while this is an interval that ends too soon we pop

            while min_heap and q > min_heap[0][1]:

                heapq.heappop(min_heap)

            if min_heap:

                res[i] = min_heap[0][0]

        return res

        #while queries > lefti we push onto the heap
        #while queries < righti we pop
        #if heap, heap[0] is res - no popping
        #else res = -1
