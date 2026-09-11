class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Greedy solution, track counts and check for invalid states
        
        High and low pointers

        Low = Least amount of unclosed open brackets if all asteriks are closing brackets
        High = Most amount of unmatched ( if each bracket is an opening bracket

        if the bracket is ( - Low and high are incremented by 1
        if the bracket is closing - both are decremented by 1
        if the bracket is * - low is decremented (an open bracket is closed) high is incremented (we create a new unmatched bracket)

        Low cannot reach negative as this would mean adding a closing before an open(instantly invalid)
        High can reach negative as this would mean a ) with nothing to the left to close it

        If high is ever negative the solution is invalid instantly
        If at the end of iteration Low = 0 and High >= 0 - just low == 0 as through iteration we check for neg high
        '''

        low = 0
        high = 0


        for bracket in s:

            if high < 0:
                return False

            if bracket == '*':
                #one less unclosed bracket
                low -= 1
                #one more unclosed bracket
                high += 1

            elif bracket == '(':
                #we are opening more brackets
                low += 1
                high += 1
            else:
                #we are closing brackets
                low -= 1
                high -= 1

            #low can never be neg as we would be creating an invalid solution by adding closing bracket before an open so instead we ignore the asterik
            if low < 0:
                low = 0
        
        #if low is zero and we didnt reach neg high valid solution
        return low == 0 and high >= 0
        
