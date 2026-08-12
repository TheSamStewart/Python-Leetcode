from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        We can't rob houses that are adjacent, now houses n-1 and 0 are adj
        '''

        n = len(nums)

        if n == 1:

            return nums[0]

        completed = dict()

        def rob(i, bound):

            if i >= bound:

                return 0

            if (i, bound) not in completed:

                rob_house = nums[i] + rob(i+2, bound)
                skip_house = rob(i+1, bound)

                completed[(i, bound)] = max(rob_house, skip_house)

            return completed[(i, bound)]

        return max(rob(0, n-1), rob(1, n))
