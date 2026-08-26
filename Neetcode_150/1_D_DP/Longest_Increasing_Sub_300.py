class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #General Approach
        #We initialise a DP array where index represents the length of the subsequence ending at this number.
        #We add numbers to our array, choosing the smallest at each step as this allows for longer future subsequences
        #If the number is larger than the end element of our array we append it.
        #We perform binary search on the dp array for quick insertion times
        #Final answer lives at the highest index present in our array
    
        
        dp = []
        
        for num in nums:

            #If num is largest yet, append to end increasing our LIS

            if not dp or num > dp[-1]:

                dp.append(num)

                continue

            #Perform binary search for insertion

            else:

                L = 0
                R = len(dp)-1
                idx = R+1
                
                while L <= R:

                    mid = (L+R)//2

                    if dp[mid] >= num:

                        idx = mid
                        R = mid-1

                    else: 
                        
                        L = mid+1

                dp[idx] = num

        #Answer is length of the array.

        return len(dp)
        
