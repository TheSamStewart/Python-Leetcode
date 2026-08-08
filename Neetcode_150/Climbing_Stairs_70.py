class Solution:
    def climbStairs(self, n: int) -> int:

        completed = dict()

        def climb(i):

            if i == n:

                return 1

            if i > n:

                return 0

            if i not in completed:

                completed[i] = climb(i+1) + climb(i+2)

            return completed[i]

        return climb(0)

            

            
        
