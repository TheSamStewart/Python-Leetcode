from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Traversal of directed graph from JFK node, breaking ties by smallest lexical order.
        
        Constraints: 
        - break ties using smallest lexical order (whichever would come first in dictionary LGA > LGB) 
        - Use a min heap, which stores nodes by lexical order - to satisfy lexical order constraint

        There is at least one valid solution 

        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        Graph theory question. Map as adjacency dict, then traverse from JFK using BFS/DFS?

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible.
        '''

        '''

        [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

        adj = {
        MUC : LHR
        JFK : MUC
        SFO : SJC
        LHR : SFO
        }

        visited = [JFK,MUC,LHR,SFO]

        res = [JFK,MUC,LHR,SFO,SJC]

        min_heap = [SJC]


        
        '''
        
        #build adj 

        adj = defaultdict(list)

        for start, end in tickets:

            heapq.heappush(adj[start], end)

        #res array 

        res = []

        def dfs(curr):

            #while we still have locations to dfs

            while adj[curr]:

                #get next destination and call dfs

                next_dest = heapq.heappop(adj[curr])

                dfs(next_dest)

            #once we have reached a dead-end this is the end (adj[curr] not truthy)of the iteniary, so this appended to res first

            res.append(curr)

        dfs("JFK")

        #reverse res to return in correct order

        return res[::-1]

