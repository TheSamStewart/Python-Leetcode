class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Starter solution.

        Starting from each index in the string

        Test all substrings starting from the smallest 
        if the palindrome test fails we can prune this part of the tree
        '''

        res = []

        def backtrack(start_idx, current_partitions):

            #BASE CASE: If palindrome append result
            if start_idx == len(s):
                res.append(current_partitions[:])
                return

            #Iterate through each char from start_idx
            for i in range(start_idx, len(s)):
               
                #Skip this part of the tree if not palindrome
                if not isPalindrome(s, start_idx, i):

                    continue 

                #Choose this substring, create slice only when we know its valid
                current_partitions.append(s[start_idx:i+1])

                #Call the function on the next starting index
                backtrack(i+1, current_partitions)

                #Then unchoose this path 
                current_partitions.pop()


        def isPalindrome(s, start_idx, i):

            L = start_idx
            R = i

            while L <= R:

                if s[L] != s[R]:

                    return False

                L += 1
                R -= 1

            return True

        backtrack(0, [])

        return res
