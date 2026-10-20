class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

      #XOR all values returns the number due to XOR property that bits compared will only return 1 if they are different

        first = nums[0]

        for num in nums[1:]:

            res = first ^ num

            first = res

        return res
        
