from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        BFS starting from each rotten orange
        queue coordinates of new and old rotten orange, or array of "rotten orange"

        first rotten orange we check adjacent squares and queue them
        mark them as orange, 
        '''

        time = 0

        #Find all oranges

        oranges = [(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 2]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #Use deque to process oranges so we can append and remove easily

        dq = deque(oranges)


        while dq:

            #rotted flag so we dont overcount

            rotted = False

            for i in range(len(dq)):

                #get current coords and increase by each direction for each coord on current level (BFS)

                current_r,current_c = dq.popleft()

                for direction_r , direction_c in directions:

                    new_r, new_c =  current_r + direction_r , current_c + direction_c

                    #check the bounds of the new coord

                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):

                        #check if this is a valid orange

                        if grid[new_r][new_c] == 1:

                            #set our rotted flag to increment time,set orange as rotted and append to queue

                            rotted = True

                            grid[new_r][new_c] = 2

                            dq.append((new_r,new_c))

            if rotted: time += 1

        #iterate through grid and check if any oranges left unrotted

        for r in range(len(grid)):

            for c in range(len(grid[0])):

                if grid[r][c] == 1:

                    return -1

        return time
