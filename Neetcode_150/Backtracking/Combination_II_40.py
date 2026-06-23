class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        sort candidates at the beggining, allowing us to ignore entire subtrees if candidate[i] > target
        sort before adding to solution set and checking if it exists
        start at target and decrement to check for valid solution
        '''

        res = []

        candidates.sort()

        def backtrack(start_idx, rem_target, current_nums):

            if rem_target == 0:

                res.append(current_nums[:])

            #explore choices starting from canidates[i]

            for i in range(start_idx, len(candidates)):

                if candidates[i] > rem_target:
                    break

                #this allows duplicate numbers at a deeper level e.g [2,2]
                #but stops us forming duplicate solutions
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue

                current_nums.append(candidates[i])

                backtrack(i+1, rem_target - candidates[i], current_nums)

                current_nums.pop()

        backtrack(0, target, [])

        return res
