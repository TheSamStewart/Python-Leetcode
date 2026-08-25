class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        cur_max = cur_min = global_max = nums[0]

        for num in nums[1:]:

          #At each index in the array calaculate the max and min subarray that ends at this point

            candidates = (num, num * cur_max, num * cur_min)

            cur_max = max(candidates)
            cur_min = min(candidates)

            global_max = max(global_max, cur_max)

        return global_max
        
