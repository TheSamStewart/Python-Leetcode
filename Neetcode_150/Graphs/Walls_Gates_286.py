from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Peform DFS on each square finding the next closest treasure (0)

        if grid[r][c] = -1, we must exit this step of recursion

        return at each stage will be int, +inf if no treasure, area if treasure found
        '''

        #init the deque with all treasure spots

        treasure = [(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]

        dq = deque(treasure)

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while dq:

            #pop the next coord to check off the deque

            r,c = dq.popleft()

            for dr,dc in directions:

                #generate each new coord

                nr , nc = r+dr, c+dc

                #check bounds

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

                    #check if square has been visited

                    if grid[nr][nc] == 2147483647:

                        #update this square treasure distance

                        grid[nr][nc] = grid[r][c] + 1

                        #append the grid coords to the deque for processing

                        dq.append((nr,nc))
