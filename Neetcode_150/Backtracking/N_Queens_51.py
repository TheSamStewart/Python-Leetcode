class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        BASE CASE:
            if n == 0 (decrement each time new queen)

        Boundaries: 
            Rows = n
            Cols = n

        Checking:
        keep count of queens Rows = for letter in grid[r]: if letter = Q count += 1 if count == 2 return 
        Cols = for row in grid : if row[c] == q count += 1 if count == 2: return
        Diagonal = check diagonals starting from row[0] and row[c] then from row[c] to row[0] to check all diagonals


        Queens cannot be placed on same row or column as another queen - check and return if criteria broken

        What is our backtrack? appending the queen in the position, then restoring once this position has been tried

        How do we generate the grid? 
        '''

        #sets for queen positions

        pos_diagonal = set()
        neg_diagonal = set() 
        cols = set()
        
        res = []

        #generate board

        board = [["."] * n for _ in range(n)]

        def backtrack(row):

            #if backtrack triggers this we have a valid solution

            if row == n:

                res.append(["".join(r) for r in board])

                return

            for c in range(0,n):

                #check if solution still valid

                if c in cols or row+c in pos_diagonal or row-c in neg_diagonal:

                    continue

                #add queen and update sets

                board[row][c] = "Q"
                cols.add(c)
                pos_diagonal.add(row+c)
                neg_diagonal.add(row-c)

                #continue down this path

                backtrack(row+1)

                #unchoose this path (backtrack)
            
                board[row][c] = "."
                cols.remove(c)
                pos_diagonal.remove(row+c)
                neg_diagonal.remove(row-c)

        backtrack(0)

        return res
