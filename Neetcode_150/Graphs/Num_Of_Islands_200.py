class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.count = 0

        #iterate through the grid
        #when we find a 1, call our function which performs DFS on all neighbouring 1 - turning all 1s to 0s
        #once all recursive function calls have returned we increment count and contine iteration

        def dfs(r,c):

            #perform boundary/end of island check(0)

            if (r >= len(grid) or r < 0
            or c >= len(grid[0]) or c < 0
            or grid[r][c] == '0'): 
                return

            #now this part of the island has been found set it to zero so we dont count it again
                
            grid[r][c] = '0'

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        #iterate through each grid position

        for r,row in enumerate(grid):

            for c,num in enumerate(row):

                #if start of island is found perform DFS

                if num == '1':

                    dfs(r,c)

                    #increment count once program returns here

                    self.count += 1

        return self.count