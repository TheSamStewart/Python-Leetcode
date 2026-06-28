class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        '''
        ROWS = len(board[0])
        COLS = len(board)

        Base Case: if word == current_word: return true

        Boundary/Used Square check:
            if r <= 0 or r >= ROWS
            or c <= 0 or c >= COLS 
            or board[r][c] == '#':
                continue

        char = board[r][c]
        
        current_word += char

        board[r][c] = '#'

        call recursive functions

        restore board at end 

        board[r][c] = char

        def search(r,c,current_word)
        
        '''

        #Define Boundaries

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,i):

            #Check if we have matched every char, if yes word found

            if i == len(word):

                return True

            #Checks for: Boundaries, Searched square or letter mismatch

            if (r < 0 or r >= ROWS
            or c < 0 or c >= COLS
            or board[r][c] == '#'
            or board[r][c] != word[i] ):
                return False

            #Save the char to restore later
                
            char = board[r][c]

            #Mark square as searched

            board[r][c] = '#'

            #Perform DFS from each surrounding square

            found = (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or 
                    dfs(r,c-1,i+1))

            #Restore board (backtrack)

            board[r][c] = char

            return found

        #Iterate through each square on the board

        for r in range(ROWS):

            for c in range(COLS):

                if dfs(r,c,0):
                    return True

        return False 
