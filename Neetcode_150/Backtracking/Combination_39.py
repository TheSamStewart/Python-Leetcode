class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        recursively call funtion on candidates[i] until current_nums sum >= target
        if sum == target then append current_nums to results array
        recursively pop off current_nums and call the function on i+1
        '''

        res = []
        current_nums = []
        
        def findSum(i, current_sum):

            #perform checks at each recurse

            if current_sum >= target or i >= len(candidates):

                if current_sum == target:

                    #use slice to create snapshot of current nums and append to the list

                    res.append(current_nums[:])

                return

            #decsion 1: choose candidates[i]

            current_nums.append(candidates[i])
            current_sum += candidates[i]
            findSum(i, current_sum)

            #backtrack: undo the selection to explore other candidates
            
            num_popped = current_nums.pop()
            current_sum -= num_popped

            #decision 2: exclude candidates[i] and move to next candidate

            findSum(i+1, current_sum)

        findSum(0,0)

        return res

           

            
