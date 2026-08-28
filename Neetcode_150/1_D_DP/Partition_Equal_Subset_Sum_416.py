class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        U - We need to find all subsets of the given array and check if any of the sums are equal
          - If they are we can just early return true
        M - DP/Recursion?
        P - criteria for correct subarray, if subarray = total / 2 it is potentially valid 

        if we find one subarray with the value total /2 it is automatically guaranteed that the other subarray also totals to total/2
        so we return the difference of our subarray and the main subarray 
        '''
        
        #find target by summing all elements in the array and / 2 - if odd impossible?

        
        total = sum(nums)

        if total % 2 != 0:

            return False

        n = len(nums)
        memo = {}
        
        def helper(remaining, i):

            #Base cases:

            if remaining == 0:

                return True
            
            if remaining < 0 or i >= n:

                return False

            if (remaining,i) in memo:

                return memo[(remaining,i)]

            #Choose and unchoose path

            res = helper(remaining - nums[i], i+1) or helper(remaining, i+1)

            #Save this part of the recursion tree to the dict

            memo[(remaining,i)] = res

            return res

        return helper(total//2, 0)

       


        
        
