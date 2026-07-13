class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Find all Os that atre touching the edge of the board

        Any Os connected to this are safe

        Any other Os need to be changed
        """

        ROWS = len(board)
        COLS = len(board[0])

        #If the current square is an O we perform DFS from here changing any connected Os to S

        def dfs(r,c):

            if (r < 0 or r >= ROWS
            or c < 0 or c >= COLS
            or board[r][c] == 'X' or board[r][c] == 'S'):

                return

            #mark safe 

            board[r][c] = 'S'

            #Check the next squares

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        
        #Loop through the border

        #Top Border
        
        for c in range(COLS):

            if board[0][c] == 'O':

                dfs(0,c)

        #Left Border

        for r in range(1, ROWS-1):

            if board[r][0] == 'O':

                dfs(r,0)

        #Bottom Border

        for c in range(COLS):

            if board[ROWS-1][c] == 'O':

                dfs(ROWS-1,c)

        #Right Border

        for r in range(1,ROWS-1):

            if board[r][COLS-1] == 'O':

                dfs(r,COLS-1)

        #Last iteration loop through the whole board, changings Os to Xs and Ss to Os

        for r in range(ROWS):

            for c in range(COLS):

                if board[r][c] == 'S':

                    board[r][c] = 'O'

                elif board[r][c] == 'O':

                    board[r][c] = 'X'

         
        
