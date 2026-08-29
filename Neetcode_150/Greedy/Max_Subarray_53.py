class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Iterate through the array holding state for max subarray at this position, min subarray and current num
        #Each iteration we find the max subarray ending here with max(num, max_subarray+num, min_subarray+num)
        # find the min by applying min to the same parameters
        #compare with a global var for max so far

        if len(nums) == 1:

            return nums[0]

        max_subarray, min_subarray = 0, 0

        res = float("-inf")

        for num in nums:

            candidate = num

            max_subarray = max(candidate, max_subarray + candidate)

            res = max(res, max_subarray)

        return res 