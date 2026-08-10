from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        We can only rob house i+2 or i+3 
        '''
        
        n = len(nums)

        @cache

        def robbery(i):

            if i >= n:

                return 0 

            return nums[i] + max(robbery(i+2), robbery(i+3))

        return max(robbery(0), robbery(1))