class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Pacific ocean = Top edge: grid[0], Left edge: grid[ALL_ROWS][0]

        Atlantic ocean = Bottom edge: grid[len(grid)] Right edge:grid[ALL_rows][len(grid[0])]

        Neighbour <= current for water to flow

        return list of coords where water can flow to pacific and atlantic ocean.
        '''

        #Create copy of grid and store a state: 0 = untouched 1 = pacific 2 = atlantic 3 = both

        grid_copy = [[0 for _ in range (len(heights[0]))] for _ in range (len(heights))]

        def pacific_check(r,c, prev_height):
            
            #Boundary Checks/Already valid path check

            if (r < 0 or r >= len(heights)
            or c < 0 or c >= len(heights[0]) 
            or grid_copy[r][c] == 1 or grid_copy[r][c] == 3):

                return

            #Check if water can flow this way

            if heights[r][c] < prev_height:

                return

            #Visit checks

            #Can't be atlantic as peforming Pacific checks first

            if grid_copy[r][c] == 0:

                grid_copy[r][c] = 1

            pacific_check(r+1,c,heights[r][c])
            pacific_check(r,c+1,heights[r][c])
            pacific_check(r-1,c,heights[r][c])
            pacific_check(r,c-1,heights[r][c])

        def atlantic_check(r,c, prev_height):

            if (r < 0 or r >= len(heights)
            or c < 0 or c >= len(heights[0]) 
            or grid_copy[r][c] == 2 or grid_copy[r][c] == 3):

                return

            if heights[r][c] < prev_height:

                return

            if grid_copy[r][c] == 0:

                grid_copy[r][c] = 2

            elif grid_copy[r][c] == 1:

                grid_copy[r][c] = 3
            
            atlantic_check(r+1,c,heights[r][c])
            atlantic_check(r,c+1,heights[r][c])
            atlantic_check(r-1,c,heights[r][c])
            atlantic_check(r,c-1,heights[r][c])

        ROWS, COLS = len(heights) , len(heights[0])

        #Pacific Checks

        for c in range(COLS):

            pacific_check(0, c, heights[0][c])

        for r in range(ROWS):

            pacific_check(r, 0, heights[r][0])

        #Atlantic Checks

        for c in range(COLS):

            atlantic_check(ROWS-1, c, heights[ROWS-1][c])

        for r in range(ROWS):

            atlantic_check(r, COLS-1, heights[r][COLS-1])

        res = []

        for r in range(ROWS):

            for c in range(COLS):

                if grid_copy[r][c] == 3:

                    res.append((r,c))

        return res
