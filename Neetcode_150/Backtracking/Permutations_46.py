class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Tracing the backtracking

        1. we swap the 1st elements to be in the 0th position of the array 
        2. we then call the backtrack on this array, which now swaps the next ith element with the next jth element
        3. when I has reached the end of the array (all swaps have occured) we append the result to our results array
        4. this then happens until the last element of the original array has been swapped to the 0th position
        '''

        res = []

        
        def backtrack(i):

            if i == len(nums):
                res.append(nums[:])

            #iterate through nums from I pointer -> len(nums)
            for j in range(i, len(nums)):

                #swap the nums
                nums[i], nums[j] = nums[j], nums[i]

                #call the function on itself incrementing I
                #this shifts the starting pointer, if I=0 - calling this function starts the J pointer at 1
                backtrack(i+1)

                #swap the nums back for next permutations
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)

        return res
