import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''

        U - Understand: Rewrite question, identify constraints, discuss assumptions and edge cases. Ask clarifying questions.

        Rewrite: Find at which value of t, we can connect grid[0][0] to [i][j]

        Constraints: 
        
        if time t = grid value we can traverse to this square

        start at square 0,0
        matrix square = elevation

        no limit in the amount of squares we can cross in 1t

        
        M - Match: Map the problem to known abstract data types (FIFO/Key-Value) or algorithmic patterns (e.g., dynamic programming, sliding window).

        Graph traversal using BFS - keeping track of t 

        P - Plan: Write pseudocode. Validate logic on paper/paint sequentially before writing code.

        mark valid squares with a #?

        I - Implement: Translate the plan into clean, production-ready code.

        R - Review: Walk through the code line-by-line using dry-run inputs.

        E - Evaluate: Analyse time and space complexity and identify potential bottlenecks.

        I – Iterate: Attempt to find a better solution if possible. 
        '''

        #Djikstra's algorithm utilises a min heap to ensure we are exploring the paths with the smallest weight (in this case time until available) first. This also means we only need to visit nodes once. Once the final node is visited this is guaranteed to be the min cost path to this node.

        #visited set to track visited nodes as they already have guaranteed min t value
        visited = set()

        #min heap to pop off next quickest available node 
        min_heap = [(grid[0][0],0,0)]

        #boundaries
        ROWS = len(grid)
        COLS = len(grid[0])

        while min_heap:

            time, r, c = heapq.heappop(min_heap)

            #we have reached the last grid square return time as min heap guarantees smallest t value
            
            if r == ROWS-1 and c == COLS-1:

                return time

            #if node already visited skip it  

            if (r,c) in visited:

                continue

            visited.add((r,c))

            #for each possible direction, perform boundary checks and visited check, if valid push to heap with new t value

            for dr , dc in [[1,0],[0,1],[-1,0],[0,-1]]:

                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited:

                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr , nc))


        
