class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Backtracking/Recusrive solution

        Use n to track parentheses added, decrement n when adding an opening parentheses

        Base case:
            n == 0:
            then check if parentheses are valid       
        '''

        res = []
        
        def backtrack(open, close, current_brackets):

            #append valid result
            
            if len(current_brackets) == n*2:

                res.append(current_brackets[:])

            #if we can, add open bracket

            if open < n:

                backtrack(open+1, close, current_brackets + "(")

            #if it doesn't break the solution, add closed bracket

            if close < open:

                backtrack(open, close+1, current_brackets + ")")
            
        backtrack(0,0,"")

        return res
        
