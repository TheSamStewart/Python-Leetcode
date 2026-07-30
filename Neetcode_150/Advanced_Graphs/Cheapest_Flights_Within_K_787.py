from collections import defaultdict

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        '''

        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Directed acylic graph

        Use Djikstra's algorithm (or an algo) to find the shortest path between src and dst with k stops

        There can be no flights

        Can a node have multiple incoming flights? this would yield a different cost, feels like it shouldnt matter

        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        min heap to sort edges with cost - also store witk k count

        adj dict to store all adj nodes and the cost of travel

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible.
        '''
        
        #Bellman ford BFS approach

        prices = [(float('inf'))] * n
        prices[src] = 0

        #Iterate through prices k time 

        for i in range(k+1):

            #Create a copy at each stage to prevent chaining of flights illegally

            temp = prices.copy()

            for u,v,price in flights:
                
                #if this triggers we havent reached this city yet so dont compute

                if prices[u] == float('inf'):
                    continue
                #otherwise we check if this is a new lowest cost

                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price

            #update prices for copying

            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1

