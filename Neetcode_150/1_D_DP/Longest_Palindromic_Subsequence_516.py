class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        U - find the longest subsequence in s in which we can delete some or no chars and it is a palindrome 
        M - DP, need to remember past work and use this information when we can
        P - 


        '''
        #1D array to map Longest Current Palindromic Subsequence between I and J
        n = len(s)
        array = [1] * n
        #As the program progresses we store the current value in a temp and update if the subsequence at this point increases

        #Iterate I through the string backwards
        for i in range(n-1,-1,-1):

            #Prev value to store the temp (already completed work)
            prev = 0
            
            #Nested J  iteration to check for LPS from I+1 to n
            for j in range(i+1,n):

                temp = array[j]

            #If our chars match DP[j] = prev + 2
                if s[j] == s[i]:
                    array[j] = prev + 2 

            #Else DP[j] = max(DP[j], DP[j-1]) - this is the max of the subsequence which exclude s[i] or excludes s[j]

                else: 
                    array[j] = max(array[j], array[j-1])

            #Update our prev value with temp - this compresses our array storing the value which excludes i and includes j without temp we would lose this as we iterate over j
                prev = temp

            #answer for LPS lives at end of the array
        return array[n-1]
