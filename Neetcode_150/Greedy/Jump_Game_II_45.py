class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Find the path in which we can reach the end of the array in the minimum amount of jumps

        Return a count 

        We can look at the next nums[i] indices, 
        '''

        n = len(nums)
        jumps = 0
        L,R  = 0,0

        while R < n-1:

            #Check for furtheST jump from L -> R slice

            furthest = max(i+nums[i] for i in range(L,R+1))

            #Move L and R pointers

            L = R + 1
            R = furthest

            jumps += 1
        
        return jumps
            
        
            
