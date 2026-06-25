class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking stratgey to create all subsets with no duplicates

        sort nums and peform i > start_idx and nums[i] == nums[i-1] check to allow duplicates at a deeper level but not solution level 
        '''

        res = []

        #sort nums to deal with duplicates
        nums.sort()

        def backtrack(start_idx, current_nums):

            #append result at each stage
            res.append(current_nums[:])

            #iterate through each number from start idx -> len nums
            #to gather each possible subset from each starting position in the array
            for i in range(start_idx, len(nums)):

                #check for duplicate
                if i > start_idx and nums[i] == nums[i-1]:
                    continue

                #choose the current element to include in the next subset branch.
                current_nums.append(nums[i])

                #call the function with the next starting boundary
                backtrack(i+1, current_nums)

                #pop the work we did off current nums for next subset
                current_nums.pop()

        backtrack(0,[])
        
        return res

        
