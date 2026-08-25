class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        #Each index in the array represents if array[0:i] can be made from wordDict

        dp = [False] * (n+1)
        dp[0] = True

        #Iterate through each index of the array

        for i in range(0,n):

            #If array up to this point can be made
            
            if dp[i] == True:

                #Check the next substring for each word in wordDict

                for word in wordDict:

                    if i + len(word) <= n and s[i:i+len(word)] == word:

                        dp[i+len(word)] = True

        #dp[n] represents whether full string exists as a combination of words in wordDict

        return dp[n] 
