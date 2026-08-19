        #Initialise an n*n matrix
        n = len(s)
        matrix = [[False] * n for _ in range(n)]
        count = 0

        #Initialise a nested loop, J loops from 0 -> n-1, I iterates from n -> 0 backwards

        for i in range(n-1,-1,-1):

            for j in range(i,n):

                if s[i] == s[j] and (j-i <= 2 or matrix[i+1][j-1]):

                    matrix[i][j] = True
                    count += 1

        return count 
